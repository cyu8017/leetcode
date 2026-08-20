// LeetCode 3725 - Count Ways to Choose Coprime Integers from Rows
// https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows/

func countCoprime(mat [][]int) int {
	const MOD = 1_000_000_007
	m := len(mat)
	// dp over gcd
	freq0 := map[int]int{}
	for _, v := range mat[0] {
		freq0[v]++
	}
	dp := freq0
	for i := 1; i < m; i++ {
		ndp := map[int]int{}
		for _, v := range mat[i] {
			for g, cnt := range dp {
				ng := gcd(g, v)
				ndp[ng] = (ndp[ng] + cnt) % MOD
			}
		}
		dp = ndp
	}
	return dp[1]
}
func gcd(a, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
