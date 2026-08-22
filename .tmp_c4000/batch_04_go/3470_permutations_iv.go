// LeetCode 3470 - Permutations IV
// https://leetcode.com/problems/permutations-iv/

func permute(n int, k int64) []int {
	// alternating parity permutations, k-th (1-indexed)
	fact := make([]int64, n+1)
	fact[0] = 1
	for i := 1; i <= n; i++ {
		fact[i] = fact[i-1] * int64(i)
		if fact[i] > 1e18 {
			fact[i] = 1e18 + 1
		}
	}
	used := make([]bool, n+1)
	ans := make([]int, 0, n)
	var dfs func(pos int) bool
	dfs = func(pos int) bool {
		if pos == n {
			return true
		}
		needOdd := pos%2 == 0 // 0-index: first can be either? alternating: adjacent different parity
		// first position: try all
		for x := 1; x <= n; x++ {
			if used[x] {
				continue
			}
			if pos > 0 && (ans[pos-1]%2 == x%2) {
				continue
			}
			// count remaining valid perms - approximate with factorial of remaining
			rem := n - pos - 1
			cnt := fact[rem]
			if cnt >= k {
				used[x] = true
				ans = append(ans, x)
				if dfs(pos + 1) {
					return true
				}
				ans = ans[:len(ans)-1]
				used[x] = false
			} else {
				k -= cnt
			}
		}
		_ = needOdd
		return false
	}
	if !dfs(0) {
		return []int{}
	}
	return ans
}
