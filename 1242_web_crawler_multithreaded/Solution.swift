// LeetCode 1242 - Web Crawler Multithreaded
// https://leetcode.com/problems/web-crawler-multithreaded/

protocol HtmlParser {
    func getUrls(_ url: String) -> [String]
}

class Solution {
    func crawl(_ startUrl: String, _ htmlParser: HtmlParser) -> [String] {
        func host(_ url: String) -> String {
            let rest = url.dropFirst("http://".count)
            if let idx = rest.firstIndex(of: "/") {
                return String(rest[..<idx])
            }
            return String(rest)
        }
        let startHost = host(startUrl)
        var seen = Set<String>([startUrl])
        var q = [startUrl]
        var qi = 0
        while qi < q.count {
            let url = q[qi]; qi += 1
            for nxt in htmlParser.getUrls(url) {
                if host(nxt) == startHost && !seen.contains(nxt) {
                    seen.insert(nxt)
                    q.append(nxt)
                }
            }
        }
        return Array(seen)
    }
}
