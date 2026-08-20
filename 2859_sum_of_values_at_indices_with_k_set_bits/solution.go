// LeetCode 2859 - Sum of Values at Indices With K Set Bits
// https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

func sumIndicesWithKSetBits(nums []int, k int) int {
	ans := 0
	for i, v := range nums {
		bits := 0
		x := i
		for x > 0 {
			bits += x & 1
			x >>= 1
		}
		if bits == k {
			ans += v
		}
	}
	return ans
}
