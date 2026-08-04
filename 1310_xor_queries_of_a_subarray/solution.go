// LeetCode 1310 - XOR Queries of a Subarray
// https://leetcode.com/problems/xor-queries-of-a-subarray/

func xorQueries(arr []int, queries [][]int) []int {
	prefix := make([]int, len(arr)+1)
	for i, x := range arr {
		prefix[i+1] = prefix[i] ^ x
	}
	answer := make([]int, len(queries))
	for i, q := range queries {
		answer[i] = prefix[q[1]+1] ^ prefix[q[0]]
	}
	return answer
}
