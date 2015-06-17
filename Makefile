all: build/

build/: clean
	blohg freeze

run: clean
	blohg freeze -s

deploy: build/
	github-pages-publish \
		--verbose \
		--cname old.rafaelmartins.eng.br \
		. \
		build/

clean:
	rm -rf build/

.PHONY: all run deploy clean
