from search import HybridIndex

PROMPT_PATH = "../prompts/task/rag_qa.md"


def build_prompt(query, hits):
    citations = []
    chunks = []
    for j, r in enumerate(hits, 1):
        citations.append(f"[{j}] {r['path']}")
        chunks.append(f"[{j}] {r['text']}")
    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        tpl = f.read()
    return (tpl
            .replace("{{query}}", query)
            .replace("{{chunks_with_ids}}", "\n\n".join(chunks))
            .replace("{{citations}}", "\n".join(citations)))


if __name__ == "__main__":
    idx = HybridIndex()
    idx.load()
    q = "우리 제품의 캐시 만료 정책?"
    hits = idx.search(q, k=8)
    print(build_prompt(q, hits))
