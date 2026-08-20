// LeetCode 0673 - Number of Longest Increasing Subsequence
// https://leetcode.com/problems/number-of-longest-increasing-subsequence/

func findNumberOfLIS(nums []int) int {
	n := len(nums)
	lengths := make([]int, n)
	counts := make([]int, n)
	for i := range lengths {
		lengths[i] = 1
		counts[i] = 1
	}
	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			if nums[j] >= nums[i] {
				continue
			}
			if lengths[j]+1 > lengths[i] {
				lengths[i] = lengths[j] + 1
				counts[i] = counts[j]
			} else if lengths[j]+1 == lengths[i] {
				counts[i] += counts[j]
			}
		}
	}
	longest := 0
	for _, length := range lengths {
		if length > longest {
			longest = length
		}
	}
	total := 0
	for i := range lengths {
		if lengths[i] == longest {
			total += counts[i]
		}
	}
	return total
}
