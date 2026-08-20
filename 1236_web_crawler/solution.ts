// LeetCode 1236 - Web Crawler
// https://leetcode.com/problems/web-crawler/

interface HtmlParser {
    getUrls(url: string): string[];
}

function crawl(startUrl: string, htmlParser: HtmlParser): string[] {
    const hostOf = (url) => {
        const u = url.replace(/^https?:\/\//, "");
        const slash = u.indexOf("/");
        return slash >= 0 ? u.slice(0, slash) : u;
    };
    const host = hostOf(startUrl);
    const seen = new Set([startUrl]);
    const stack = [startUrl];
    while (stack.length) {
        const cur = stack.pop();
        for (const url of htmlParser.getUrls(cur)) {
            if (hostOf(url) === host && !seen.has(url)) {
                seen.add(url);
                stack.push(url);
            }
        }
    }
    return [...seen].sort();
}
