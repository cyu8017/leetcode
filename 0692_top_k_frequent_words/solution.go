// LeetCode 0692 - Top K Frequent Words
// https://leetcode.com/problems/top-k-frequent-words/

import "sort"

func topKFrequent(words []string, k int) []string {
	counts := map[string]int{}
	for _, w := range words {
		counts[w]++
	}
	ordered := make([]string, 0, len(counts))
	for w := range counts {
		ordered = append(ordered, w)
	}
	sort.Slice(ordered, func(i, j int) bool {
		if counts[ordered[i]] == counts[ordered[j]] {
			return ordered[i] < ordered[j]
		}
		return counts[ordered[i]] > counts[ordered[j]]
	})
	return ordered[:k]
}
