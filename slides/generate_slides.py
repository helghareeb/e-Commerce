#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CHAPTER_DIR = ROOT / "src" / "chapters"
SLIDES_SRC_DIR = ROOT / "slides" / "src"

TITLE = (
    r"An Introduction to E-Commerce\\\small with a Focus on Machine Learning, "
    r"Deep Learning, and Artificial Intelligence"
)
AUTHOR = r"Dr. Haitham A. El-Ghareeb"
INSTITUTE = r"Faculty of Computers and Information Sciences \\ Mansoura University \\ Egypt"

IGNORE_SECTIONS = {
    "learning objectives",
    "multiple-choice questions (mcqs)",
    "exercises (short)",
    "mini-case (odoo-linked, vendor-neutral)",
    "case studies (placeholder)",
    "hands-on artifacts",
    "artifacts for this chapter",
}

INCLUDE_TAIL_SECTIONS = {
    "hands-on (placeholder)",
    "hands-on lab: build a minimal metrics layer",
    "hands-on lab: modeling an order lifecycle",
    "hands-on lab: a baseline recommender",
    "hands-on lab: retrieval plus re-ranking",
    "hands-on lab: forecast plus constrained optimization",
    "hands-on lab: risk scoring and thresholding",
    "hands-on lab: a grounded faq and service assistant",
    "hands-on lab: assessing an ai returns assistant",
    "managerial implications",
    "managerial and architectural implications",
    "final reflection",
}


def clean_inline(text: str) -> str:
    text = text.strip()
    text = re.sub(r"%.*", "", text)
    text = text.replace("``", '"').replace("''", '"')
    text = re.sub(r"\\cite[p|t]?\{[^}]*\}", "", text)
    text = re.sub(r"\\label\{[^}]*\}", "", text)
    text = re.sub(r"\\ref\{[^}]*\}", "reference", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def section_chunks(text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"\\section\{([^}]*)\}", text))
    chunks: list[tuple[str, str]] = []
    for idx, match in enumerate(matches):
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        title = clean_inline(match.group(1))
        body = text[start:end]
        chunks.append((title, body))
    return chunks


def item_blocks(body: str) -> list[str]:
    items: list[str] = []
    for block in re.finditer(r"\\begin\{itemize\}(.*?)\\end\{itemize\}", body, re.S):
        for item in block.group(1).split(r"\item")[1:]:
            cleaned = clean_inline(item)
            if cleaned:
                items.append(cleaned)
    for block in re.finditer(r"\\begin\{enumerate\}(.*?)\\end\{enumerate\}", body, re.S):
        for item in block.group(1).split(r"\item")[1:]:
            cleaned = clean_inline(item)
            if cleaned and len(cleaned) < 180:
                items.append(cleaned)
    return items


def subsection_items(body: str) -> list[str]:
    out: list[str] = []
    matches = list(re.finditer(r"\\subsection\{([^}]*)\}", body))
    for idx, match in enumerate(matches):
        title = clean_inline(match.group(1))
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(body)
        block = body[start:end]
        bullets = item_blocks(block)
        if bullets:
            snippet = "; ".join(bullets[:2])
            out.append(rf"\textbf{{{title}:}} {snippet}")
        else:
            if ("\\[" in block or "$" in block) and title.lower() == "basic idea":
                out.append(
                    rf"\textbf{{{title}:}} Learn latent user and item factors, then score items from their interaction strength."
                )
                continue
            sentence = first_sentences(block, 1)
            if sentence:
                out.append(rf"\textbf{{{title}:}} {sentence[0]}")
    return out


def first_sentences(body: str, limit: int) -> list[str]:
    stripped = re.sub(r"\\begin\{.*?\\end\{.*?}", " ", body, flags=re.S)
    stripped = re.sub(r"\\\[.*?\\\]", " ", stripped, flags=re.S)
    stripped = re.sub(r"\$[^$]*\$", " ", stripped)
    stripped = re.sub(r"\\subsection\{[^}]*\}", " ", stripped)
    stripped = re.sub(r"\\begin\{itemize\}.*?\\end\{itemize\}", " ", stripped, flags=re.S)
    stripped = re.sub(r"\\begin\{enumerate\}.*?\\end\{enumerate\}", " ", stripped, flags=re.S)
    stripped = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^]]*\])?(?:\{[^}]*\})?", " ", stripped)
    stripped = clean_inline(stripped)
    if not stripped:
        return []
    candidates = re.split(r"(?<=[.!?])\s+", stripped)
    out: list[str] = []
    for sentence in candidates:
        sentence = clean_inline(sentence)
        if len(sentence) < 25:
            continue
        out.append(sentence)
        if len(out) >= limit:
            break
    return out


def extract_learning_objectives(text: str) -> list[str]:
    for title, body in section_chunks(text):
        if title.lower() == "learning objectives":
            return item_blocks(body)[:5]
    return []


def chapter_title(text: str) -> str:
    match = re.search(r"\\chapter(?:\[[^]]*\])?\{([^}]*)\}", text)
    if not match:
        raise ValueError("Missing chapter title")
    return clean_inline(match.group(1))


def lecture_sections(text: str) -> list[tuple[str, list[str]]]:
    selected: list[tuple[str, list[str]]] = []
    for title, body in section_chunks(text):
        lowered = title.lower()
        if lowered in IGNORE_SECTIONS:
            continue
        bullets = subsection_items(body)
        if not bullets:
            bullets = item_blocks(body)
        if not bullets:
            bullets = first_sentences(body, 3)
        bullets = [bullet for bullet in bullets if bullet][:6]
        if not bullets:
            continue
        if lowered in INCLUDE_TAIL_SECTIONS or (
            "mcq" not in lowered and "exercise" not in lowered and "mini-case" not in lowered
        ):
            selected.append((title, bullets))
    return selected


def session_plan_items(sections: list[tuple[str, list[str]]]) -> list[str]:
    substantive = []
    tail = []
    for title, _ in sections:
        lowered = title.lower()
        if lowered in INCLUDE_TAIL_SECTIONS:
            tail.append(title)
        else:
            substantive.append(title)
    plan = substantive[:5]
    if tail:
        plan.append(tail[0])
    return plan[:6]


def make_tex(number: int, chapter: str, objectives: list[str], sections: list[tuple[str, list[str]]]) -> str:
    short = f"Lecture {number:02d}"
    plan = session_plan_items(sections)
    lines = [
        r"\documentclass[aspectratio=169]{beamer}",
        r"\usetheme{Madrid}",
        r"\usecolortheme{default}",
        r"\usepackage{amsmath}",
        r"\usepackage{graphicx}",
        r"\usepackage{tikz-cd}",
        r"\usepackage{multicol}",
        "",
        r"\setlength{\parindent}{0pt}",
        r"\setlength{\parskip}{1\baselineskip}",
        "",
        rf"\title[{short}]{{{TITLE}}}",
        rf"\subtitle{{Lecture {number:02d}: {chapter}}}",
        rf"\author{{{AUTHOR}}}",
        rf"\institute{{{INSTITUTE}}}",
        r"\date{\today}",
        "",
        r"\begin{document}",
        "",
        r"\begin{frame}",
        r"  \titlepage",
        r"\end{frame}",
        "",
        r"\begin{frame}{Session plan (90 minutes)}",
        r"  \begin{enumerate}",
    ]
    for item in plan:
        lines.append(f"    \\item {item}")
    lines.extend(
        [
            r"  \end{enumerate}",
            r"\end{frame}",
            "",
        ]
    )
    if objectives:
        lines.extend(
            [
                r"\begin{frame}{Learning objectives}",
                r"  By the end of this lecture, you should be able to:",
                r"  \begin{itemize}",
            ]
        )
        for item in objectives:
            lines.append(f"    \\item {item}")
        lines.extend([r"  \end{itemize}", r"\end{frame}", ""])

    for idx, (title, bullets) in enumerate(sections, start=1):
        lines.append(rf"\section{{{title}}}")
        lines.append("")
        lines.append(rf"\begin{{frame}}{{{title}}}")
        lines.append(r"  \begin{itemize}")
        for bullet in bullets:
            lines.append(f"    \\item {bullet}")
        lines.append(r"  \end{itemize}")
        lines.append(r"\end{frame}")
        lines.append("")

    lines.extend([r"\end{document}", ""])
    return "\n".join(lines)


def main() -> None:
    chapters = sorted(CHAPTER_DIR.glob("ch*.tex"))
    for idx, chapter_file in enumerate(chapters, start=1):
        if idx == 1:
            continue
        text = chapter_file.read_text(encoding="utf-8")
        title = chapter_title(text)
        objectives = extract_learning_objectives(text)
        sections = lecture_sections(text)
        target = SLIDES_SRC_DIR / f"{idx:02d}.tex"
        target.write_text(make_tex(idx, title, objectives, sections), encoding="utf-8")
        print(f"wrote {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
