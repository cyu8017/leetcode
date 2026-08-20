// LeetCode 2740 - Find the Value of the Partition
// https://leetcode.com/problems/find-the-value-of-the-partition/


import "sort"

func findValueOfPartition(nums []int) int {
	sort.Ints(nums)
	ans := nums[1] - nums[0]
	for i := 2; i < len(nums); i++ {
		d := nums[i] - nums[i-1]
		if d < ans {
			ans = d
		}
	}
	return ans
}
