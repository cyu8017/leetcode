// LeetCode 3281 - Maximize Score of Numbers in Ranges
// https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

import "sort"

func maxPossibleScore(start []int, d int) int {
	sort.Ints(start)
	n := len(start)
	ok := func(mid int) bool {
		prev := int64(start[0])
		for i := 1; i < n; i++ {
			need := prev + int64(mid)
			cur := int64(start[i])
			if need > cur+int64(d) {
				return false
			}
			if need > cur {
				prev = need
			} else {
				prev = cur
			}
		}
		return true
	}
	lo, hi := 0, int(start[n-1])+d-start[0]+1
	for lo < hi {
		mid := (lo + hi + 1) / 2
		if ok(mid) {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	return lo
}
