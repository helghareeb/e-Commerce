# AI-Driven E-Commerce Systems

This repository contains the LaTeX source for the book *AI-Driven E-Commerce Systems: Architecture, Data, Intelligence, and Operations*. The manuscript covers platform strategy, enterprise architecture, data foundations, AI and ML applications, ERP integration, governance, and a final capstone architecture.

The current cover metadata identifies the book as authored by **Haitham A. El-Ghareeb**, Associate Professor, Information Systems Department, Faculty of Computers and Information Sciences, Mansoura University, Egypt.

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
- `src/main.pdf`: compiled output PDF.
- `src/references_2.bib`: bibliography database used by the manuscript.
- `NEXT-STEPS.md`: handoff notes and continuation guidance between sessions.

## Current Manuscript Status

The repository currently contains:

- an unnumbered preface;
- a 14-chapter continuous manuscript;
- appendices and bibliography support;
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
- Several long chapter titles use shortened running-head forms in LaTeX to keep page headers clean while preserving full chapter titles in the text.
- Generated LaTeX artifacts such as `main.aux`, `main.out`, `main.toc`, and `main.pdf` are currently tracked in the repository.
