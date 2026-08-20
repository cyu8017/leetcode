// LeetCode 0811 - Subdomain Visit Count
// https://leetcode.com/problems/subdomain-visit-count/

import (
	"fmt"
	"strconv"
	"strings"
)

func subdomainVisits(cpdomains []string) []string {
	counts := map[string]int{}
	for _, item := range cpdomains {
		parts := strings.Fields(item)
		count, _ := strconv.Atoi(parts[0])
		domain := parts[1]
		segs := strings.Split(domain, ".")
		for i := 0; i < len(segs); i++ {
			counts[strings.Join(segs[i:], ".")] += count
		}
	}
	ans := make([]string, 0, len(counts))
	for domain, count := range counts {
		ans = append(ans, fmt.Sprintf("%d %s", count, domain))
	}
	return ans
}
