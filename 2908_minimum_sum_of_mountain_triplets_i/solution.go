// LeetCode 2908 - Minimum Sum of Mountain Triplets I
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/

func minimumSum(nums []int) int {
	n := len(nums)
	ans := 1 << 30
	for j := 1; j < n-1; j++ {
		left, right := 1<<30, 1<<30
		for i := 0; i < j; i++ {
			if nums[i] < nums[j] && nums[i] < left {
				left = nums[i]
			}
		}
		for k := j + 1; k < n; k++ {
			if nums[k] < nums[j] && nums[k] < right {
				right = nums[k]
			}
		}
		if left < 1<<30 && right < 1<<30 {
			cand := left + nums[j] + right
			if cand < ans {
				ans = cand
			}
		}
	}
	if ans == 1<<30 {
		return -1
	}
	return ans
}
