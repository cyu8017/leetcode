// LeetCode 3700 - Number of ZigZag Arrays II
// https://leetcode.com/problems/number-of-zigzag-arrays-ii/

func zigZagArrays(n int, l int, r int) int {
	const MOD = 1_000_000_007
	m := r - l + 1
	if n == 1 {
		return m % MOD
	}
	up := make([]int, m)
	down := make([]int, m)
	for j := 0; j < m; j++ {
		up[j], down[j] = 1, 1
	}
	for length := 2; length <= n; length++ {
		pref := make([]int, m+1)
		for j := 0; j < m; j++ {
			pref[j+1] = (pref[j] + down[j]) % MOD
		}
		nup := make([]int, m)
		for j := 0; j < m; j++ {
			nup[j] = pref[j]
		}
		suf := make([]int, m+1)
		for j := m - 1; j >= 0; j-- {
			suf[j] = (suf[j+1] + up[j]) % MOD
		}
		ndown := make([]int, m)
		for j := 0; j < m; j++ {
			ndown[j] = suf[j+1]
		}
		up, down = nup, ndown
	}
	ans := 0
	for j := 0; j < m; j++ {
		ans = (ans + up[j]) % MOD
		ans = (ans + down[j]) % MOD
	}
	return ans
}
