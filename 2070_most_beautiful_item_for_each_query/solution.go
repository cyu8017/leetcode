// LeetCode 2070 - Most Beautiful Item for Each Query
// https://leetcode.com/problems/most-beautiful-item-for-each-query/

import "sort"

func maximumBeauty(items [][]int, queries []int) []int {
	sort.Slice(items, func(i, j int) bool { return items[i][0] < items[j][0] })
	maxB := 0
	for _, it := range items {
		if it[1] > maxB {
			maxB = it[1]
		}
		it[1] = maxB
	}
	ans := make([]int, len(queries))
	for i, q := range queries {
		lo, hi := 0, len(items)
		for lo < hi {
			mid := (lo + hi) / 2
			if items[mid][0] <= q {
				lo = mid + 1
			} else {
				hi = mid
			}
		}
		if lo == 0 {
			ans[i] = 0
		} else {
			ans[i] = items[lo-1][1]
		}
	}
	return ans
}
