// LeetCode 2317 - Maximum XOR After Operations
// https://leetcode.com/problems/maximum-xor-after-operations/

func maximumXOR(nums []int) int {
	ans := 0
	for _, x := range nums {
		ans |= x
	}
	return ans
}
