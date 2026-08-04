// LeetCode 1420 - Build Array Where You Can Find The Maximum Exactly K Comparisons
// https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/

func numOfArrays(n int, m int, k int) int {
	const mod = 1000000007
	dp := make([][]int, k+1)
	for i := range dp {
		dp[i] = make([]int, m+1)
	}
	for maximum := 1; maximum <= m; maximum++ {
		dp[1][maximum] = 1
	}
	for length := 1; length < n; length++ {
		nxt := make([][]int, k+1)
		for i := range nxt {
			nxt[i] = make([]int, m+1)
		}
		for cost := 1; cost <= k; cost++ {
			prefix := 0
			for maximum := 1; maximum <= m; maximum++ {
				prefix = (prefix + dp[cost-1][maximum-1]) % mod
				nxt[cost][maximum] = (maximum*dp[cost][maximum] + prefix) % mod
			}
		}
		dp = nxt
	}
	ans := 0
	for _, v := range dp[k] {
		ans = (ans + v) % mod
	}
	return ans
}
