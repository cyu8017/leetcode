// LeetCode 2576 - Find the Maximum Number of Marked Indices
// https://leetcode.com/problems/find-the-maximum-number-of-marked-indices/


import "sort"

func maxNumOfMarkedIndices(nums []int) int {
	sort.Ints(nums)
	n := len(nums)
	i, ans := 0, 0
	for j := (n + 1) / 2; j < n; j++ {
		if 2*nums[i] <= nums[j] {
			ans += 2
			i++
		}
	}
	return ans
}
