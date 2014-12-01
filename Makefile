NAME = trento
PDF = $(NAME).pdf
SRC = $(NAME).tex $(NAME).bib duke-qcd-refs/Duke_QCD_refs.bib
FIGS = $(wildcard fig/*.pdf)
BUILDDIR = build
LATEX = latexmk -pdf -halt-on-error -synctex=1 -output-directory=$(BUILDDIR)

.PHONY: all clean distclean

all: $(PDF)

$(PDF): $(SRC) $(FIGS)
	$(LATEX) $(NAME)
	mv $(BUILDDIR)/$(PDF) .

clean:
	rm -rf $(BUILDDIR)

distclean: clean
	rm -f $(PDF)
