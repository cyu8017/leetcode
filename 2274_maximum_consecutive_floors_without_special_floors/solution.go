// LeetCode 2274 - Maximum Consecutive Floors Without Special Floors
// https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/

import "sort"

func maxConsecutive(bottom int, top int, special []int) int {
	sort.Ints(special)
	ans := special[0] - bottom
	for i := 1; i < len(special); i++ {
		if special[i]-special[i-1]-1 > ans {
			ans = special[i] - special[i-1] - 1
		}
	}
	if top-special[len(special)-1] > ans {
		ans = top - special[len(special)-1]
	}
	return ans
}
