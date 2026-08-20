// LeetCode 2411 - Smallest Subarrays With Maximum Bitwise OR
// https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

func smallestSubarrays(nums []int) []int {
	n := len(nums)
	ans := make([]int, n)
	last := make([]int, 32)
	for i := range last {
		last[i] = -1
	}
	for i := n - 1; i >= 0; i-- {
		for b := 0; b < 32; b++ {
			if (nums[i]>>b)&1 == 1 {
				last[b] = i
			}
		}
		far := i
		for b := 0; b < 32; b++ {
			if last[b] > far {
				far = last[b]
			}
		}
		ans[i] = far - i + 1
	}
	return ans
}
