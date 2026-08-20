// LeetCode 0995 - Minimum Number of K Consecutive Bit Flips
// https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

func minKBitFlips(nums []int, k int) int {
	n := len(nums)
	flip := make([]int, n)
	ans, flipped := 0, 0
	for i, bit := range nums {
		if i >= k {
			flipped ^= flip[i-k]
		}
		if bit == flipped {
			if i+k > n {
				return -1
			}
			ans++
			flipped ^= 1
			flip[i] = 1
		}
	}
	return ans
}
