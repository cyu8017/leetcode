// LeetCode 0581 - Shortest Unsorted Continuous Subarray
// https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

func findUnsortedSubarray(nums []int) int {
	n := len(nums)
	left, right := -1, -2
	maxSeen, minSeen := nums[0], nums[n-1]
	for i := 0; i < n; i++ {
		if nums[i] > maxSeen {
			maxSeen = nums[i]
		}
		if nums[i] < maxSeen {
			right = i
		}
		j := n - 1 - i
		if nums[j] < minSeen {
			minSeen = nums[j]
		}
		if nums[j] > minSeen {
			left = j
		}
	}
	return right - left + 1
}
