// LeetCode 1438 - Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
// https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

func longestSubarray(nums []int, limit int) int {
	low, high := []int{}, []int{}
	left, answer := 0, 0
	for right, value := range nums {
		for len(low) > 0 && nums[low[len(low)-1]] > value {
			low = low[:len(low)-1]
		}
		for len(high) > 0 && nums[high[len(high)-1]] < value {
			high = high[:len(high)-1]
		}
		low = append(low, right)
		high = append(high, right)
		for nums[high[0]]-nums[low[0]] > limit {
			left++
			if low[0] < left {
				low = low[1:]
			}
			if high[0] < left {
				high = high[1:]
			}
		}
		if right-left+1 > answer {
			answer = right - left + 1
		}
	}
	return answer
}
