NAME = trento
PDF = $(NAME).pdf
SRC = $(NAME).tex
BUILDDIR = build
LATEX = latexmk -pdf -output-directory=$(BUILDDIR)

all: $(PDF)

$(PDF): $(SRC)
	$(LATEX) $(NAME)
	mv $(BUILDDIR)/$(PDF) .

clean:
	rm -rf $(BUILDDIR)
