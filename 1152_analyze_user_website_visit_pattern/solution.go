// LeetCode 1152 - Analyze User Website Visit Pattern
// https://leetcode.com/problems/analyze-user-website-visit-pattern/

import "sort"

func mostVisitedPattern(username []string, timestamp []int, website []string) []string {
	type visit struct {
		t    int
		site string
	}
	visits := map[string][]visit{}
	for i := range username {
		visits[username[i]] = append(visits[username[i]], visit{timestamp[i], website[i]})
	}
	scores := map[[3]string]int{}
	for _, vs := range visits {
		sort.Slice(vs, func(i, j int) bool { return vs[i].t < vs[j].t })
		sites := make([]string, len(vs))
		for i, v := range vs {
			sites[i] = v.site
		}
		patterns := map[[3]string]bool{}
		for i := 0; i < len(sites); i++ {
			for j := i + 1; j < len(sites); j++ {
				for k := j + 1; k < len(sites); k++ {
					patterns[[3]string{sites[i], sites[j], sites[k]}] = true
				}
			}
		}
		for p := range patterns {
			scores[p]++
		}
	}
	var best [3]string
	bestCount := -1
	first := true
	for p, c := range scores {
		if first || c > bestCount || (c == bestCount && (p[0] < best[0] || (p[0] == best[0] && (p[1] < best[1] || (p[1] == best[1] && p[2] < best[2]))))) {
			best, bestCount, first = p, c, false
		}
	}
	return []string{best[0], best[1], best[2]}
}
