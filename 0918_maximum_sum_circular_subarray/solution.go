// LeetCode 0918 - Maximum Sum Circular Subarray
// https://leetcode.com/problems/maximum-sum-circular-subarray/

func maxSubarraySumCircular(nums []int) int {
	total := nums[0]
	maxSum, minSum := nums[0], nums[0]
	curMax, curMin := nums[0], nums[0]
	for _, x := range nums[1:] {
		total += x
		if curMax+x > x {
			curMax = curMax + x
		} else {
			curMax = x
		}
		if curMin+x < x {
			curMin = curMin + x
		} else {
			curMin = x
		}
		if curMax > maxSum {
			maxSum = curMax
		}
		if curMin < minSum {
			minSum = curMin
		}
	}
	if maxSum < 0 {
		return maxSum
	}
	circ := total - minSum
	if circ > maxSum {
		return circ
	}
	return maxSum
}
