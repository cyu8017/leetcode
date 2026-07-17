// LeetCode 1835 - Find XOR Sum of All Pairs Bitwise AND
// https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/

func getXORSum(arr1 []int, arr2 []int) int {
	xor1, xor2 := 0, 0
	for _, value := range arr1 {
		xor1 ^= value
	}
	for _, value := range arr2 {
		xor2 ^= value
	}
	return xor1 & xor2
}
