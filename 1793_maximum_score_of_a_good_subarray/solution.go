// LeetCode 1793 - Maximum Score of a Good Subarray
// https://leetcode.com/problems/maximum-score-of-a-good-subarray/

func maximumScore(nums []int, k int) int {
	n := len(nums)
	stack := []int{}
	ans := 0
	for i := 0; i <= n; i++ {
		for len(stack) > 0 && (i == n || nums[i] < nums[stack[len(stack)-1]]) {
			mid := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			left := 0
			if len(stack) > 0 {
				left = stack[len(stack)-1] + 1
			}
			right := i - 1
			if left <= k && k <= right {
				score := nums[mid] * (right - left + 1)
				if score > ans {
					ans = score
				}
			}
		}
		stack = append(stack, i)
	}
	return ans
}
