// LeetCode 0338 - Counting Bits
// https://leetcode.com/problems/counting-bits/

func countBits(n int) []int {
	result := make([]int, n+1)
	for index := 1; index <= n; index++ {
		result[index] = result[index&(index-1)] + 1
	}
	return result
}
