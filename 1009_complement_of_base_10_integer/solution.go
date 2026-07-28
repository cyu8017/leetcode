// LeetCode 1009 - Complement of Base 10 Integer
// https://leetcode.com/problems/complement-of-base-10-integer/

func bitwiseComplement(n int) int {
	if n == 0 {
		return 1
	}
	mask := 1
	for mask <= n {
		mask <<= 1
	}
	return n ^ (mask - 1)
}
