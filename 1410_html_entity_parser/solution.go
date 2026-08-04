// LeetCode 1410 - HTML Entity Parser
// https://leetcode.com/problems/html-entity-parser/

import "strings"

func entityParser(text string) string {
	entities := [][2]string{
		{"&quot;", `"`},
		{"&apos;", "'"},
		{"&gt;", ">"},
		{"&lt;", "<"},
		{"&frasl;", "/"},
		{"&amp;", "&"},
	}
	// Replace &amp; last
	for _, e := range entities[:5] {
		text = strings.ReplaceAll(text, e[0], e[1])
	}
	text = strings.ReplaceAll(text, "&amp;", "&")
	return text
}
