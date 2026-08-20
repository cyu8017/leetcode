// LeetCode 3255 - Find the Power of K-Size Subarrays II
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-ii/

func resultsArray(nums []int, k int) []int {
	n := len(nums)
	ans := make([]int, n-k+1)
	if k == 1 {
		copy(ans, nums)
		return ans
	}
	streak := 1
	for i := 1; i < n; i++ {
		if nums[i] == nums[i-1]+1 {
			streak++
		} else {
			streak = 1
		}
		if i >= k-1 {
			if streak >= k {
				ans[i-k+1] = nums[i]
			} else {
				ans[i-k+1] = -1
			}
		}
	}
	return ans
}
