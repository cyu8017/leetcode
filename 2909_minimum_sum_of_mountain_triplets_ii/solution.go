// LeetCode 2909 - Minimum Sum of Mountain Triplets II
// https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/

func minimumSum(nums []int) int {
	n := len(nums)
	left := make([]int, n)
	right := make([]int, n)
	mn := 1 << 30
	for i := 0; i < n; i++ {
		left[i] = mn
		if nums[i] < mn {
			mn = nums[i]
		}
	}
	mn = 1 << 30
	for i := n - 1; i >= 0; i-- {
		right[i] = mn
		if nums[i] < mn {
			mn = nums[i]
		}
	}
	ans := 1 << 30
	for j := 1; j < n-1; j++ {
		if left[j] < nums[j] && right[j] < nums[j] {
			cand := left[j] + nums[j] + right[j]
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
