// LeetCode 1236 - Web Crawler
// https://leetcode.com/problems/web-crawler/

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
	stack := []string{startUrl}
	for len(stack) > 0 {
		cur := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		for _, url := range htmlParser.GetUrls(cur) {
			if hostOf(url) == host && !seen[url] {
				seen[url] = true
				stack = append(stack, url)
			}
		}
	}
	ans := make([]string, 0, len(seen))
	for u := range seen {
		ans = append(ans, u)
	}
	sort.Strings(ans)
	return ans
}
