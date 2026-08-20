// LeetCode 3254 - Find the Power of K-Size Subarrays I
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

func resultsArray(nums []int, k int) []int {
	n := len(nums)
	ans := make([]int, n-k+1)
	for i := 0; i <= n-k; i++ {
		ok := true
		for j := i + 1; j < i+k; j++ {
			if nums[j] != nums[j-1]+1 {
				ok = false
				break
			}
		}
		if ok {
			ans[i] = nums[i+k-1]
		} else {
			ans[i] = -1
		}
	}
	return ans
}
