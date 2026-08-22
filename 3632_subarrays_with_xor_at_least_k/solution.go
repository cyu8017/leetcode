// LeetCode 3632 - Subarrays With XOR At Least K
// https://leetcode.com/problems/subarrays-with-xor-at-least-k/

func subarraysWithXorAtLeastK(nums []int, k int) int64 {
	n := len(nums)
	var ans int64
	for i := 0; i < n; i++ {
		x := 0
		for j := i; j < n; j++ {
			x ^= nums[j]
			if x >= k {
				ans++
			}
		}
	}
	return ans
}
