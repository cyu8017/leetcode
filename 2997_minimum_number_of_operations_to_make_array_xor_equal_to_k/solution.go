// LeetCode 2997 - Minimum Number of Operations to Make Array XOR Equal to K
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

func minOperations(nums []int, k int) int {
	xorr := 0
	for _, v := range nums {
		xorr ^= v
	}
	diff := xorr ^ k
	ans := 0
	for diff > 0 {
		ans += diff & 1
		diff >>= 1
	}
	return ans
}
