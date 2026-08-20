// LeetCode 2563 - Count the Number of Fair Pairs
// https://leetcode.com/problems/count-the-number-of-fair-pairs/


import "sort"

func countFairPairs(nums []int, lower int, upper int) int64 {
	sort.Ints(nums)
	count := func(x int) int64 {
		var ans int64
		l, r := 0, len(nums)-1
		for l < r {
			if nums[l]+nums[r] <= x {
				ans += int64(r - l)
				l++
			} else {
				r--
			}
		}
		return ans
	}
	return count(upper) - count(lower-1)
}
