// LeetCode 0693 - Binary Number with Alternating Bits
// https://leetcode.com/problems/binary-number-with-alternating-bits/

func hasAlternatingBits(n int) bool {
	x := n ^ (n >> 1)
	return x&(x+1) == 0
}
