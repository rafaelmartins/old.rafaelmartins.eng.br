all: build/

build/:
	blohg freeze

deploy: build/
	github-pages-publish \
		--verbose \
		--cname old.rafaelmartins.eng.br \
		. \
		build/

clean:
	rm -rf build/

.PHONY: all deploy clean
