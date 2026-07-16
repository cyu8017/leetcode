from urllib.parse import urlsplit

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> list[str]:
        host = urlsplit(startUrl).netloc
        seen, stack = {startUrl}, [startUrl]
        while stack:
            for url in htmlParser.getUrls(stack.pop()):
                if urlsplit(url).netloc == host and url not in seen:
                    seen.add(url)
                    stack.append(url)
        return sorted(seen)
