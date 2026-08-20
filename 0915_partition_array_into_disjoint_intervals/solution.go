// LeetCode 0915 - Partition Array Into Disjoint Intervals
// https://leetcode.com/problems/partition-array-into-disjoint-intervals/

func partitionDisjoint(nums []int) int {
	n := len(nums)
	minRight := make([]int, n)
	minRight[n-1] = nums[n-1]
	for i := n - 2; i >= 0; i-- {
		minRight[i] = nums[i]
		if minRight[i+1] < minRight[i] {
			minRight[i] = minRight[i+1]
		}
	}
	maxLeft := nums[0]
	for i := 1; i < n; i++ {
		if maxLeft <= minRight[i] {
			return i
		}
		if nums[i] > maxLeft {
			maxLeft = nums[i]
		}
	}
	return n - 1
}
