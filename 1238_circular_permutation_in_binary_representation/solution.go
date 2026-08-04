// LeetCode 1238 - Circular Permutation in Binary Representation
// https://leetcode.com/problems/circular-permutation-in-binary-representation/

func circularPermutation(n int, start int) []int {
	ans := make([]int, 1<<n)
	for i := 0; i < 1<<n; i++ {
		ans[i] = start ^ i ^ (i >> 1)
	}
	return ans
}
