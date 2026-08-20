// LeetCode 2896 - Apply Operations to Make Two Strings Equal
// https://leetcode.com/problems/apply-operations-to-make-two-strings-equal/

func minOperations(s1 string, s2 string, x int) int {
	diff := []int{}
	for i := 0; i < len(s1); i++ {
		if s1[i] != s2[i] {
			diff = append(diff, i)
		}
	}
	m := len(diff)
	if m%2 == 1 {
		return -1
	}
	if m == 0 {
		return 0
	}
	dp := make([]int, m+1)
	for i := range dp {
		dp[i] = 1 << 30
	}
	dp[0] = 0
	for i := 0; i < m; i++ {
		if dp[i] == 1<<30 {
			continue
		}
		// pair with next
		if i+1 < m {
			cost := diff[i+1] - diff[i]
			if x < cost {
				cost = x
			}
			// actually adjacent flip cost 1, or general x
			cost = diff[i+1] - diff[i]
			if cost > x {
				cost = x
			}
			if dp[i]+cost < dp[i+2] {
				dp[i+2] = dp[i] + cost
			}
		}
	}
	// better DP
	for i := range dp {
		dp[i] = 1 << 30
	}
	dp[0] = 0
	for i := 2; i <= m; i += 2 {
		for j := 0; j < i; j += 2 {
			// cost to fix diff[j:i]
		}
	}
	// O(m^2)
	f := make([]int, m+1)
	for i := range f {
		f[i] = 1 << 30
	}
	f[0] = 0
	for i := 0; i < m; i++ {
		if f[i] == 1<<30 {
			continue
		}
		for j := i + 1; j < m; j += 2 {
			// pair i..j as one group using x repeatedly? 
		}
		// take pair i,i+1
		if i+1 < m {
			c := diff[i+1] - diff[i]
			if c > x {
				c = x
			}
			if f[i]+c < f[i+2] {
				f[i+2] = f[i] + c
			}
		}
	}
	// also allow paying x for any pair not adjacent in value
	// Standard: dp[i] min cost for first i diffs
	dp2 := make([]int, m+1)
	for i := range dp2 {
		dp2[i] = 1 << 30
	}
	dp2[0] = 0
	for i := 0; i < m; i++ {
		if dp2[i] >= 1<<30 {
			continue
		}
		if i+1 < m {
			c := diff[i+1] - diff[i]
			if x < c*1 {
				// use x once for any two
			}
			cand := diff[i+1] - diff[i]
			if cand > x {
				cand = x
			}
			if dp2[i]+cand < dp2[i+2] {
				dp2[i+2] = dp2[i] + cand
			}
		}
	}
	if dp2[m] >= 1<<30 {
		return -1
	}
	return dp2[m]
}
