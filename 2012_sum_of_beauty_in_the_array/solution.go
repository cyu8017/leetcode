// LeetCode 2012 - Sum of Beauty in the Array
// https://leetcode.com/problems/sum-of-beauty-in-the-array/

func sumOfBeauties(nums []int) int {
	n := len(nums)
	prefixMax := make([]int, n)
	suffixMin := make([]int, n)
	prefixMax[0] = nums[0]
	for i := 1; i < n; i++ {
		prefixMax[i] = prefixMax[i-1]
		if nums[i] > prefixMax[i] {
			prefixMax[i] = nums[i]
		}
	}
	suffixMin[n-1] = nums[n-1]
	for i := n - 2; i >= 0; i-- {
		suffixMin[i] = suffixMin[i+1]
		if nums[i] < suffixMin[i] {
			suffixMin[i] = nums[i]
		}
	}
	ans := 0
	for i := 1; i < n-1; i++ {
		if prefixMax[i-1] < nums[i] && nums[i] < suffixMin[i+1] {
			ans += 2
		} else if nums[i-1] < nums[i] && nums[i] < nums[i+1] {
			ans++
		}
	}
	return ans
}
