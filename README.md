# AI-Driven E-Commerce Systems

This repository contains the LaTeX source for the book *AI-Driven E-Commerce Systems: Architecture, Data, Intelligence, and Operations*. The manuscript covers platform strategy, enterprise architecture, data foundations, AI and ML applications, ERP integration, governance, and a final capstone architecture.

The current cover metadata identifies the book as authored by **Haitham A. El-Ghareeb**, Associate Professor, Information Systems Department, Faculty of Computers and Information Sciences, Mansoura University, Egypt.

## License and Reuse

The content of this repository is licensed under **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.

This means readers may:

- read, download, copy, print, and share the material;
- reuse and adapt the material for educational and other non-commercial purposes;
- redistribute excerpts or derived educational material, provided attribution is preserved.

This also means users must:

- credit **Haitham A. El-Ghareeb** as the author;
- reference this repository when reusing the content;
- link to the CC BY-NC 4.0 license;
- indicate whether changes were made;
- not use the repository content for commercial purposes without separate permission.

Recommended attribution:

```text
Haitham A. El-Ghareeb, AI-Driven E-Commerce Systems: Architecture, Data, Intelligence, and Operations, GitHub repository: https://github.com/helghareeb/e-Commerce
```

See [LICENSE](LICENSE) for the repository license text and [CITATION.cff](CITATION.cff) for citation metadata.

## Project Nature

The manuscript is written as a continuous book rather than a slide deck or disconnected weekly notes. Its scope combines:

- digital commerce business models and platform thinking;
- enterprise architecture and system integration;
- Odoo-centered ERP/CRM/SCM process integration;
- data engineering, experimentation, and analytics foundations;
- recommendation, pricing, fraud, LLM support, and MLOps;
- security, privacy, compliance, and responsible AI.

## Repository Structure

- `src/main.tex`: main LaTeX entry point for the book.
- `src/chapters/`: individual chapter source files.
- `src/backmatter/`: unnumbered end-of-book reference and assessment chapters.
- `src/main.pdf`: compiled output PDF.
- `src/references_2.bib`: bibliography database used by the manuscript.
- `NEXT-STEPS.md`: handoff notes and continuation guidance between sessions.

## Current Manuscript Status

The repository currently contains:

- an unnumbered preface;
- a 14-chapter continuous manuscript;
- appendices;
- unnumbered back-matter chapters for acronyms and sample essay questions;
- bibliography support;
- a compiled PDF in `src/main.pdf`.

The chapter sequence covers:

1. Foundations of modern e-commerce systems
2. Digital platforms and business models
3. Data foundations, experimentation, and metrics
4. Enterprise architecture for e-commerce
5. Enterprise integration patterns
6. ERP/CRM/SCM integration with Odoo as reference
7. Classical recommenders and learning-to-rank
8. Deep recommenders and retrieval systems
9. Pricing and promotion analytics
10. Fraud, risk, and trust and safety
11. LLM-based customer service and support automation
12. MLOps and DataOps for e-commerce
13. Security, privacy, compliance, and responsible AI
14. Capstone enterprise-grade AI e-commerce architecture

The current back matter also includes:

- `Acronyms and Key Abbreviations`
- `Sample Essay Questions and Model Answers`

## Build

Compile from the `src/` directory:

```bash
pdflatex -interaction=nonstopmode main.tex
bibtex main
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```

Use the full sequence above when bibliography entries change or new citations are added.
If only text changes are made without bibliography updates, two `pdflatex` passes are usually enough.

## Notes

- The manuscript now uses `src/references_2.bib` with BibTeX and `plainnat` for citations and references.
- The front matter has been converted to a proper preface, so Chapter 1 is the first numbered chapter in the book.
- The chapter titles no longer carry `(Week ...)` suffixes; the chapter numbers already provide sequencing.
- Several long chapter titles use shortened running-head forms in LaTeX to keep page headers clean while preserving full chapter titles in the text.
- Generated LaTeX build intermediates are ignored; source files and selected compiled PDFs remain in the repository.
