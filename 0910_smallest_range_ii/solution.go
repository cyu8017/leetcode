// LeetCode 0910 - Smallest Range II
// https://leetcode.com/problems/smallest-range-ii/

import "sort"

func smallestRangeII(nums []int, k int) int {
	sort.Ints(nums)
	ans := nums[len(nums)-1] - nums[0]
	for i := 0; i < len(nums)-1; i++ {
		lo := nums[0] + k
		if nums[i+1]-k < lo {
			lo = nums[i+1] - k
		}
		hi := nums[len(nums)-1] - k
		if nums[i]+k > hi {
			hi = nums[i] + k
		}
		if hi-lo < ans {
			ans = hi - lo
		}
	}
	return ans
}
