// LeetCode 3685 - Subsequence Sum After Capping Elements
// https://leetcode.com/problems/subsequence-sum-after-capping-elements/

import (
	"sort"
)

func subsequenceSumAfterCapping(nums []int, k int) []bool {
	n := len(nums)
	sorted := append([]int(nil), nums...)
	sort.Ints(sorted)
	ans := make([]bool, n)
	reach := make([]bool, k+1)
	reach[0] = true
	idx := 0
	for x := 1; x <= n; x++ {
		for idx < n && sorted[idx] <= x {
			v := sorted[idx]
			for s := k; s >= v; s-- {
				if reach[s-v] {
					reach[s] = true
				}
			}
			idx++
		}
		tmp := append([]bool(nil), reach...)
		rem := n - idx
		for s := 0; s <= k; s++ {
			if !reach[s] {
				continue
			}
			for t := 1; t <= rem && s+t*x <= k; t++ {
				tmp[s+t*x] = true
			}
		}
		ans[x-1] = tmp[k]
	}
	return ans
}
