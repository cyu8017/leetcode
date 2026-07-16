// LeetCode 0451 - Sort Characters By Frequency
// https://leetcode.com/problems/sort-characters-by-frequency/

import "sort"

func frequencySort(s string) string {
	counts := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		counts[s[i]]++
	}

	type pair struct {
		ch  byte
		cnt int
	}
	ordered := make([]pair, 0, len(counts))
	for ch, cnt := range counts {
		ordered = append(ordered, pair{ch, cnt})
	}
	sort.Slice(ordered, func(i, j int) bool {
		if ordered[i].cnt != ordered[j].cnt {
			return ordered[i].cnt > ordered[j].cnt
		}
		return ordered[i].ch < ordered[j].ch
	})

	result := make([]byte, 0, len(s))
	for _, item := range ordered {
		for k := 0; k < item.cnt; k++ {
			result = append(result, item.ch)
		}
	}
	return string(result)
}
