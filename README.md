# AI-Driven E-Commerce Systems

This repository contains the LaTeX source for a full book on modern e-commerce systems, covering platform strategy, enterprise architecture, data foundations, AI and ML applications, ERP integration, governance, and a final capstone architecture.

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

The repository currently contains a 14-chapter manuscript plus appendices. The chapter sequence covers:

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
pdflatex -interaction=nonstopmode main.tex
```

Two passes are typically needed for the table of contents and PDF outline to settle.

## Notes

- The bibliography file `src/references_2.bib` is currently empty, so citation keys render as question marks until entries are added and BibTeX is run.
- Generated LaTeX artifacts such as `main.aux`, `main.out`, `main.toc`, and `main.pdf` are currently tracked in the repository.
