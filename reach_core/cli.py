import argparse
from .scraper import MultiScraper
from .cache import Cache

def main():
    p = argparse.ArgumentParser(description="reach-core")
    p.add_argument("command", choices=["search"])
    p.add_argument("query")
    p.add_argument("--sources", default="x,reddit,github")
    p.add_argument("--days", type=int, default=30)
    args = p.parse_args()

    cache = Cache()
    scraper = MultiScraper(cache=cache)
    sources = [s.strip() for s in args.sources.split(",")]
    result = scraper.search(args.query, sources=sources, days=args.days)
    print(result)
