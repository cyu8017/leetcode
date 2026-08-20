// LeetCode 0873 - Length of Longest Fibonacci Subsequence
// https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

func lenLongestFibSubseq(arr []int) int {
	index := map[int]int{}
	for i, x := range arr {
		index[x] = i
	}
	n := len(arr)
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, n)
		for j := range dp[i] {
			dp[i][j] = 2
		}
	}
	ans := 0
	for j := 0; j < n; j++ {
		for i := 0; i < j; i++ {
			if k, ok := index[arr[j]-arr[i]]; ok && k < i {
				dp[i][j] = dp[k][i] + 1
				if dp[i][j] > ans {
					ans = dp[i][j]
				}
			}
		}
	}
	if ans >= 3 {
		return ans
	}
	return 0
}
