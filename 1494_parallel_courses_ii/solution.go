// LeetCode 1494 - Parallel Courses II
// https://leetcode.com/problems/parallel-courses-ii/

func minNumberOfSemesters(n int, relations [][]int, k int) int {
	prereq := make([]int, n)
	for _, r := range relations {
		prereq[r[1]-1] |= 1 << (r[0] - 1)
	}
	full := (1 << n) - 1
	const inf = int(1e9)
	dp := make([]int, 1<<n)
	for i := range dp {
		dp[i] = inf
	}
	dp[0] = 0
	bitCount := func(x int) int {
		c := 0
		for x > 0 {
			c += x & 1
			x >>= 1
		}
		return c
	}
	for mask := 0; mask < 1<<n; mask++ {
		if dp[mask] == inf {
			continue
		}
		available := 0
		for c := 0; c < n; c++ {
			if mask>>c&1 == 0 && prereq[c]&mask == prereq[c] {
				available |= 1 << c
			}
		}
		var choices []int
		if bitCount(available) <= k {
			choices = []int{available}
		} else {
			for sub := available; sub > 0; sub = (sub - 1) & available {
				if bitCount(sub) == k {
					choices = append(choices, sub)
				}
			}
		}
		for _, take := range choices {
			next := mask | take
			if dp[mask]+1 < dp[next] {
				dp[next] = dp[mask] + 1
			}
		}
	}
	return dp[full]
}
