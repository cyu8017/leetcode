// LeetCode 1879 - Minimum XOR Sum of Two Arrays
// https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

import "math/bits"

func minimumXORSum(nums1 []int, nums2 []int) int {
	n := len(nums1)
	size := 1 << n
	dp := make([]int, size)
	for i := 1; i < size; i++ {
		dp[i] = 1 << 30
	}

	for mask := 0; mask < size; mask++ {
		i := bits.OnesCount(uint(mask))
		if i >= n {
			continue
		}
		for j := 0; j < n; j++ {
			if mask&(1<<j) != 0 {
				continue
			}
			nextMask := mask | (1 << j)
			cost := dp[mask] + (nums1[i] ^ nums2[j])
			if cost < dp[nextMask] {
				dp[nextMask] = cost
			}
		}
	}

	return dp[size-1]
}
