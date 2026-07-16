// LeetCode 0371 - Sum of Two Integers
// https://leetcode.com/problems/sum-of-two-integers/

func getSum(a int, b int) int {
	mask := uint32(0xFFFFFFFF)

	for b != 0 {
		carry := uint32(a&b) << 1
		a = int((uint32(a^b) & mask))
		b = int(carry & mask)
	}

	if a <= 0x7FFFFFFF {
		return a
	}
	return int(^(uint32(a) ^ mask))
}
