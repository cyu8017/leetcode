// LeetCode 2657 - Find the Prefix Common Array of Two Arrays
// https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/


func findThePrefixCommonArray(A []int, B []int) []int {
	n := len(A)
	seenA, seenB := make([]bool, n+1), make([]bool, n+1)
	ans := make([]int, n)
	common := 0
	for i := 0; i < n; i++ {
		if seenB[A[i]] {
			common++
		}
		seenA[A[i]] = true
		if seenA[B[i]] {
			common++
		}
		seenB[B[i]] = true
		ans[i] = common
	}
	return ans
}
