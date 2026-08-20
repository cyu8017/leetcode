// LeetCode 2683 - Neighboring Bitwise XOR
// https://leetcode.com/problems/neighboring-bitwise-xor/


func doesValidArrayExist(derived []int) bool {
	x := 0
	for _, v := range derived {
		x ^= v
	}
	return x == 0
}
