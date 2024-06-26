##################################################
# Makefile is used as shortcut holder
# type 'make' to get all target documentation
##################################################

# HELP
# This will output the help for each task
# thanks to https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z0-9_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ">> make info << for more details"

localTry: ## cmd line test
	python ./try.py

localStart: ## start pyBird API without docker
	python -m flask run --host=0.0.0.0 --port=8000

localCall: ## ask predict using local API
	curl -X POST -H "Content-Type: application/json" -H "PRIVATE-KEY: blahblah23" \
		-d '{"url": "https://images.pexels.com/photos/326900/pexels-photo-326900.jpeg?cs=srgb&dl=pexels-pixabay-326900.jpg&fm=jpg"}'\
		http://127.0.0.1:8000/bioclip/predict
