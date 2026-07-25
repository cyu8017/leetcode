// LeetCode 1611 - Minimum One Bit Operations to Make Integers Zero
// https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/

func minimumOneBitOperations(n int) int {
	ans := 0
	for n > 0 {
		ans ^= n
		n >>= 1
	}
	return ans
}
