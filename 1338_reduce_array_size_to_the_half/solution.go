// LeetCode 1338 - Reduce Array Size to The Half
// https://leetcode.com/problems/reduce-array-size-to-the-half/

import "sort"

func minSetSize(arr []int) int {
	counts := map[int]int{}
	for _, v := range arr {
		counts[v]++
	}
	freqs := make([]int, 0, len(counts))
	for _, f := range counts {
		freqs = append(freqs, f)
	}
	sort.Sort(sort.Reverse(sort.IntSlice(freqs)))
	removed := 0
	for i, frequency := range freqs {
		removed += frequency
		if removed*2 >= len(arr) {
			return i + 1
		}
	}
	return 0
}
