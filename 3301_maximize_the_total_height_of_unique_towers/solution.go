// LeetCode 3301 - Maximize the Total Height of Unique Towers
// https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/

import "sort"

func maximumTotalSum(maximumHeight []int) int64 {
	sort.Sort(sort.Reverse(sort.IntSlice(maximumHeight)))
	var ans int64
	prev := int(1e18)
	for _, h := range maximumHeight {
		cur := h
		if cur >= prev {
			cur = prev - 1
		}
		if cur <= 0 {
			return -1
		}
		ans += int64(cur)
		prev = cur
	}
	return ans
}
