// LeetCode 2813 - Maximum Elegance of a K-Length Subsequence
// https://leetcode.com/problems/maximum-elegance-of-a-k-length-subsequence/

import "sort"

func findMaximumElegance(items [][]int, k int) int64 {
	sort.Slice(items, func(i, j int) bool { return items[i][0] > items[j][0] })
	seen := map[int]bool{}
	var total int64
	dup := []int{}
	for i := 0; i < k; i++ {
		total += int64(items[i][0])
		c := items[i][1]
		if seen[c] {
			dup = append(dup, items[i][0])
		} else {
			seen[c] = true
		}
	}
	ans := total + int64(len(seen))*int64(len(seen))
	for i := k; i < len(items); i++ {
		c := items[i][1]
		if seen[c] || len(dup) == 0 {
			continue
		}
		total += int64(items[i][0]) - int64(dup[len(dup)-1])
		dup = dup[:len(dup)-1]
		seen[c] = true
		cand := total + int64(len(seen))*int64(len(seen))
		if cand > ans {
			ans = cand
		}
	}
	return ans
}
