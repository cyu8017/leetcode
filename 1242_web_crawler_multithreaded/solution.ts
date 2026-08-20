// LeetCode 1242 - Web Crawler Multithreaded
// https://leetcode.com/problems/web-crawler-multithreaded/

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
    let frontier = [startUrl];
    while (frontier.length) {
        const next = [];
        for (const cur of frontier) {
            for (const url of htmlParser.getUrls(cur)) {
                if (hostOf(url) === host && !seen.has(url)) {
                    seen.add(url);
                    next.push(url);
                }
            }
        }
        frontier = next;
    }
    return [...seen].sort();
}
