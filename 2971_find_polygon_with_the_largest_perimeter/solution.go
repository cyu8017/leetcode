// LeetCode 2971 - Find Polygon With the Largest Perimeter
// https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/

import "sort"

func largestPerimeter(nums []int) int64 {
	sort.Ints(nums)
	var sum int64
	for _, v := range nums {
		sum += int64(v)
	}
	for i := len(nums) - 1; i >= 2; i-- {
		sum -= int64(nums[i])
		if sum > int64(nums[i]) {
			return sum + int64(nums[i])
		}
	}
	return -1
}
