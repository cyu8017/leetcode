// LeetCode 3699 - Number of ZigZag Arrays I
// https://leetcode.com/problems/number-of-zigzag-arrays-i/

func zigZagArrays(n int, l int, r int) int {
	const MOD = 1_000_000_007
	m := r - l + 1
	if n == 1 {
		return m % MOD
	}
	up := make([]int, m)
	down := make([]int, m)
	for j := 0; j < m; j++ {
		up[j] = 1
		down[j] = 1
	}
	for len_ := 2; len_ <= n; len_++ {
		prefDown := make([]int, m+1)
		for j := 0; j < m; j++ {
			prefDown[j+1] = (prefDown[j] + down[j]) % MOD
		}
		nup := make([]int, m)
		for j := 0; j < m; j++ {
			nup[j] = prefDown[j]
		}
		sufUp := make([]int, m+1)
		for j := m - 1; j >= 0; j-- {
			sufUp[j] = (sufUp[j+1] + up[j]) % MOD
		}
		ndown := make([]int, m)
		for j := 0; j < m; j++ {
			ndown[j] = sufUp[j+1]
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
