// LeetCode 2420 - Find All Good Indices
// https://leetcode.com/problems/find-all-good-indices/

func goodIndices(nums []int, k int) []int {
	n := len(nums)
	dec := make([]int, n)
	inc := make([]int, n)
	dec[0] = 1
	for i := 1; i < n; i++ {
		if nums[i] <= nums[i-1] {
			dec[i] = dec[i-1] + 1
		} else {
			dec[i] = 1
		}
	}
	inc[n-1] = 1
	for i := n - 2; i >= 0; i-- {
		if nums[i] <= nums[i+1] {
			inc[i] = inc[i+1] + 1
		} else {
			inc[i] = 1
		}
	}
	ans := []int{}
	for i := k; i < n-k; i++ {
		if dec[i-1] >= k && inc[i+1] >= k {
			ans = append(ans, i)
		}
	}
	return ans
}
