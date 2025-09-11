import glob
import json
import os
import re


def read_texts(root):
    paths = []
    for ext in ("*.md", "*.txt"):
        paths += glob.glob(os.path.join(root, "**", ext), recursive=True)
    for p in paths:
        with open(p, "r", encoding="utf-8", errors="ignore") as f:
            yield p, f.read()


def chunk(text, size=600, overlap=80):
    tokens = re.findall(r"\S+\s*", text)
    i = 0
    while i < len(tokens):
        yield "".join(tokens[i:i + size])
        i += size - overlap


def contextualize_chunk(title, section, chunk_text):
    # Anthropic Contextual Retrieval: 청크 앞에 문맥 주석(50~100 토큰 권장) [Source](https://www.anthropic.com/news/contextual-retrieval)
    prefix = f"[DOC={title}] [SECTION={section}] "
    return prefix + chunk_text


def build_corpus(src="./knowledge_base", out="corpus.jsonl"):
    items = []
    for path, full in read_texts(src):
        title = os.path.basename(path)
        sections = re.split(r"\n#{1,6}\s+", full) if path.endswith(".md") else [full]
        for sec in sections:
            for ch in chunk(sec):
                txt = contextualize_chunk(title, "auto", ch)
                items.append({"path": path, "text": txt})
    with open(out, "w", encoding="utf-8") as f:
        for it in items:
            f.write(json.dumps(it, ensure_ascii=False) + "\n")
    print(f"built {len(items)} chunks → {out}")


if __name__ == "__main__":
    os.makedirs("./knowledge_base", exist_ok=True)
    build_corpus()
