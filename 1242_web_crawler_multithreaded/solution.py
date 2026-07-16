from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlsplit

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> list[str]:
        host, seen, frontier = urlsplit(startUrl).netloc, {startUrl}, [startUrl]
        with ThreadPoolExecutor() as pool:
            while frontier:
                next_frontier = []
                for urls in pool.map(htmlParser.getUrls, frontier):
                    for url in urls:
                        if urlsplit(url).netloc == host and url not in seen:
                            seen.add(url)
                            next_frontier.append(url)
                frontier = next_frontier
        return sorted(seen)
