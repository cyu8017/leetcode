// LeetCode 3920 - Maximize Fixed Points After Deletions
// https://leetcode.com/problems/maximize-fixed-points-after-deletions/

import "sort"

func maxFixedPoints(nums []int) int {
	tails := make([]int, 0)
	for i, x := range nums {
		if i < x {
			continue
		}
		d := i - x
		p := sort.SearchInts(tails, d)
		if p == len(tails) {
			tails = append(tails, d)
		} else {
			tails[p] = d
		}
	}
	return len(tails)
}