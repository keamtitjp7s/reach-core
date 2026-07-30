class MultiScraper:
    def __init__(self, cache=None):
        self.cache = cache

    def search(self, query, sources=None, days=30):
        sources = sources or ["x", "reddit", "github"]
        results = []
        for src in sources:
            key = f"{src}:{query}:{days}"
            if self.cache and self.cache.get(key):
                results.append(self.cache.get(key))
                continue
            item = {
                "source": src,
                "query": query,
                "days": days,
                "items": [{"title": f"Sample from {src}", "url": f"https://{src}.example/{query}", "snippet": "..."}],
                "sentiment": 0.1,
                "entities": [query]
            }
            if self.cache:
                self.cache.set(key, item)
            results.append(item)
        return {"query": query, "results": results, "citation_graph": []}
