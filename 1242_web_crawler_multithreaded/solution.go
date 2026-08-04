// LeetCode 1242 - Web Crawler Multithreaded
// https://leetcode.com/problems/web-crawler-multithreaded/

import "sort"
import "strings"

type HtmlParser interface {
	GetUrls(url string) []string
}

func crawl(startUrl string, htmlParser HtmlParser) []string {
	hostOf := func(url string) string {
		u := strings.TrimPrefix(url, "http://")
		if i := strings.IndexByte(u, '/'); i >= 0 {
			return u[:i]
		}
		return u
	}
	host := hostOf(startUrl)
	seen := map[string]bool{startUrl: true}
	frontier := []string{startUrl}
	for len(frontier) > 0 {
		next := []string{}
		for _, cur := range frontier {
			for _, url := range htmlParser.GetUrls(cur) {
				if hostOf(url) == host && !seen[url] {
					seen[url] = true
					next = append(next, url)
				}
			}
		}
		frontier = next
	}
	ans := make([]string, 0, len(seen))
	for u := range seen {
		ans = append(ans, u)
	}
	sort.Strings(ans)
	return ans
}
