// LeetCode 1486 - XOR Operation in an Array
// https://leetcode.com/problems/xor-operation-in-an-array/

func xorOperation(n int, start int) int {
	ans := 0
	for i := 0; i < n; i++ {
		ans ^= start + 2*i
	}
	return ans
}
