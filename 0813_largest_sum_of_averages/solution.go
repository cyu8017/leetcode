// LeetCode 0813 - Largest Sum of Averages
// https://leetcode.com/problems/largest-sum-of-averages/

func largestSumOfAverages(nums []int, k int) float64 {
	n := len(nums)
	prefix := make([]float64, n+1)
	for i, num := range nums {
		prefix[i+1] = prefix[i] + float64(num)
	}
	average := func(i, j int) float64 {
		return (prefix[j] - prefix[i]) / float64(j-i)
	}
	dp := make([]float64, n)
	for i := 0; i < n; i++ {
		dp[i] = average(0, i+1)
	}
	for groups := 2; groups <= k; groups++ {
		nxt := make([]float64, n)
		for i := groups - 1; i < n; i++ {
			best := 0.0
			for j := groups - 2; j < i; j++ {
				cand := dp[j] + average(j+1, i+1)
				if cand > best {
					best = cand
				}
			}
			nxt[i] = best
		}
		dp = nxt
	}
	return dp[n-1]
}
