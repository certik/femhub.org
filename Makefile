OUTDIR=output

HTML=$(wildcard templates/*.html)

CSS=$(wildcard css/*)
IMG=$(wildcard img/*)

all: html copy

html: $(HTML)
	python generate.py

copy: $(CSS) $(IMG)
	cp -r css $(OUTDIR)
	cp -r img $(OUTDIR)

.PHONY: clean

clean:
	rm -rf $(OUTDIR)/*

