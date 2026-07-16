// LeetCode 0190 - Reverse Bits
// https://leetcode.com/problems/reverse-bits/

func reverseBits(n uint32) uint32 {
	var result uint32
	for bit := 0; bit < 32; bit++ {
		result = (result << 1) | (n & 1)
		n >>= 1
	}
	return result
}