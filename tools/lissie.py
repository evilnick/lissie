#!/usr/bin/env python
"""
A tool to handle mass convertion of Markdown
docs into a website.
"""

# imports
import os
import sys
import shutil
import markdown
import argparse
import fnmatch
import re
import codecs
from configobj import ConfigObj

# Functions

def recursive_overwrite(src, dest, ignore=None):
    if os.path.isdir(src):
        if not os.path.isdir(dest):
            os.makedirs(dest)
        files = os.listdir(src)
        if ignore is not None:
            ignored = ignore(src, files)
        else:
            ignored = set()
        for f in files:
            if f not in ignored:
                recursive_overwrite(os.path.join(src, f), 
                                    os.path.join(dest, f), 
                                    ignore)
    else:
        shutil.copyfile(src, dest)

def getargs():
    d_text = """MD to whatever docs processor"""
    parser = argparse.ArgumentParser(description=d_text)
    parser.add_argument('--config', nargs=1, dest='configfile', \
     default=['default.cfg'], help="config file to load")
    parser.add_argument('--source', nargs=1, default='./src', help="source directory")
    parser.add_argument('--debug', dest='debug',action='store_true')
    return (parser.parse_args())  

def read_config(configfile):
    #TODO check if file exists   
    config=ConfigObj(configfile)
    return(config)

    
def main():
    
    args = getargs()   
    configfile=args.configfile[0]
    config=read_config(configfile)
    sourcedir=args.source[0]
    if args.debug :
        print 'Using config:'
        print config
    #check for metadata key
    if 'meta' in config['extensions'] :
        metaparse=True
    else:
        print "***WARNING: Meta extension not used, any metadata in source files will \
              be processed into the output ***"
    # create markdown parser from config. This will be  reset and reused for each page
    ext_configs = {'meta': []}
    
    mdparser = markdown.Markdown(output_format=config['outformat'], extensions=['meta'])
    # make outdir
    outdir=os.path.abspath(config['output_dir'])
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    #copy media and includes
    recursive_overwrite(os.path.join(sourcedir,config['media_dir']),os.path.join(outdir,'media'))
    recursive_overwrite(os.path.join(sourcedir,config['css_dir']),os.path.join(outdir,'includes/css'))
    recursive_overwrite(os.path.join(sourcedir,config['js_dir']),os.path.join(outdir,'includes/js'))   
    # loop through dirs checking for md content
    for dir in os.listdir(sourcedir) :
        
        if os.path.isdir(os.path.join(sourcedir,dir)):
            
            for file in os.listdir(os.path.join(sourcedir,dir)):
               if fnmatch.fnmatch(file, '*.md'):
                  if args.debug :
                     print "processing ..."+file
                  page=Page(os.path.join(sourcedir,dir,file), args,mdparser,config)
                  page.process()
                  page.write(os.path.join(outdir,dir,file))
                  
    
    # process dirs
    
    
# Classes
class docs:
    """A complete set of docs"""
    

class Page:
    """A page of data"""
    
    def __init__(self, filename, args, mdparser, config):
        self.filename=filename
        self.content = ''
        self.args = args
        self.parser=mdparser
        self.config=config
        self.load_content()
        
    def load_content(self):
    	i=codecs.open(self.filename, mode="r", encoding="utf-8")
        self.content = i.read()
        
    def process(self):
        sourcedir= self.args.source[0]
        content= self.parser.convert(self.content)
        #extract metadata
        title=' - '.join([self.config['sitename'],self.parser.Meta['title'][0]])
        #load template
        t=open(os.path.join(sourcedir,os.path.join(self.config['templates_dir'],'Template')))
        self.output = t.read()
        #replace tokens
        replace= [ ('%%TITLE%%', title),                       \
                   ('%%CSS%%', '.'+self.config['css_dir']),    \
                   ('%%JS%%', '.'+self.config['js_dir']),      \
                   ('%%CONTENT%%', content)     \
                 ]
        for pair in replace:
            self.output = re.sub(pair[0], pair[1], self.output)
            
        #reset the parser for next use
        self.parser.reset()
        
    def write(self,filepath):
        filepath = os.path.splitext(filepath)[0]+'.html'
        if not os.path.exists(os.path.dirname(filepath)):
            os.makedirs(os.path.dirname(filepath))
        file=codecs.open(filepath,"w",encoding="utf-8",errors="xmlcharrefreplace")
        file.write(self.output)
        file.close
    
if __name__ == "__main__":
    main()
