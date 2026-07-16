// LeetCode 0239 - Sliding Window Maximum
// https://leetcode.com/problems/sliding-window-maximum/

func maxSlidingWindow(nums []int, k int) []int {
	window := make([]int, 0)
	result := make([]int, 0, len(nums)-k+1)

	for index, num := range nums {
		for len(window) > 0 && nums[window[len(window)-1]] <= num {
			window = window[:len(window)-1]
		}
		window = append(window, index)
		if window[0] <= index-k {
			window = window[1:]
		}
		if index >= k-1 {
			result = append(result, nums[window[0]])
		}
	}

	return result
}
