SOURCE_DIR= ./src
BUILD_DIR= ./build
TESTBUILDER= markdown_py 
BUILDER= ./tools/lissie.py


docs:
	mkdir -p $(BUILD_DIR)
	$(BUILDER) --source $(SOURCE_DIR) --config='tools/default.cfg' --debug
    
test: $(SOURCE_DIR)/test.md 

	mkdir -p $(BUILD_DIR)
	$(TESTBUILDER) -x meta $(SOURCE_DIR)/test.md > $(BUILD_DIR)/test.html
	python -m SimpleHTTPServer 

clean:
	@rm -rf build
	@find . -iname "*~" -exec rm '{}' ';'
