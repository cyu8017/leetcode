// LeetCode 2465 - Number of Distinct Averages
// https://leetcode.com/problems/number-of-distinct-averages/

import "sort"

func distinctAverages(nums []int) int {
	sort.Ints(nums)
	seen := map[int]bool{}
	l, r := 0, len(nums)-1
	for l < r {
		seen[nums[l]+nums[r]] = true
		l++
		r--
	}
	return len(seen)
}
