// LeetCode 3575 - Maximum Good Subtree Score
// https://leetcode.com/problems/maximum-good-subtree-score/

func goodSubtreeSum(vals []int, par []int) int {
	const MOD = 1_000_000_007
	n := len(vals)
	g := make([][]int, n)
	for i := 1; i < n; i++ {
		g[par[i]] = append(g[par[i]], i)
	}
	ans := 0
	digitMask := func(x int) (int, bool, int) {
		v := x
		mask := 0
		if x == 0 {
			return 1, true, 0
		}
		for x > 0 {
			d := x % 10
			if mask&(1<<d) != 0 {
				return 0, false, 0
			}
			mask |= 1 << d
			x /= 10
		}
		return mask, true, v
	}
	var dfs func(u int) map[int]int
	dfs = func(u int) map[int]int {
		dp := map[int]int{0: 0}
		mask, ok, v := digitMask(vals[u])
		if ok {
			dp[mask] = v
		}
		for _, c := range g[u] {
			child := dfs(c)
			ndp := map[int]int{}
			for m1, s1 := range dp {
				for m2, s2 := range child {
					if m1&m2 == 0 {
						nm := m1 | m2
						if s1+s2 > ndp[nm] {
							ndp[nm] = s1 + s2
						}
					}
				}
			}
			for m, s := range dp {
				if s > ndp[m] {
					ndp[m] = s
				}
			}
			for m, s := range child {
				if s > ndp[m] {
					ndp[m] = s
				}
			}
			dp = ndp
		}
		best := 0
		for _, s := range dp {
			if s > best {
				best = s
			}
		}
		ans = (ans + best) % MOD
		return dp
	}
	dfs(0)
	return ans
}
