// LeetCode 0698 - Partition to K Equal Sum Subsets
// https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

import "sort"

func canPartitionKSubsets(nums []int, k int) bool {
	total := 0
	for _, num := range nums {
		total += num
	}
	if total%k != 0 {
		return false
	}
	target := total / k
	sort.Sort(sort.Reverse(sort.IntSlice(nums)))
	if nums[0] > target {
		return false
	}
	buckets := make([]int, k)
	var dfs func(index int) bool
	dfs = func(index int) bool {
		if index == len(nums) {
			return true
		}
		for i := 0; i < k; i++ {
			if buckets[i]+nums[index] > target {
				continue
			}
			buckets[i] += nums[index]
			if dfs(index + 1) {
				return true
			}
			buckets[i] -= nums[index]
			if buckets[i] == 0 {
				break
			}
		}
		return false
	}
	return dfs(0)
}
