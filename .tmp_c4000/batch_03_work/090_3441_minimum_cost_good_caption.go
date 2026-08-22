// LeetCode 3441 - Minimum Cost Good Caption
// https://leetcode.com/problems/minimum-cost-good-caption/

func minCostGoodCaption(caption string) string {
	n := len(caption)
	if n < 3 {
		return ""
	}
	// greedy make runs of length >= 3
	b := []byte(caption)
	const inf = int(1e18)
	// DP change to char groups
	type state struct {
		cost int
		prev int
		ch   byte
		len  int
	}
	// Simplified: for each position force groups of 3+
	ans := make([]byte, n)
	copy(ans, b)
	i := 0
	for i < n {
		j := i
		for j < n && ans[j] == ans[i] {
			j++
		}
		if j-i >= 3 {
			i = j
			continue
		}
		// extend or change
		need := 3 - (j - i)
		if j+need <= n {
			for t := 0; t < need; t++ {
				ans[j+t] = ans[i]
			}
			i = j + need
		} else {
			// change this run to neighbor
			ch := byte('a')
			if i > 0 {
				ch = ans[i-1]
			} else if j < n {
				ch = b[j]
			}
			for t := i; t < n; t++ {
				ans[t] = ch
			}
			break
		}
	}
	// verify
	i = 0
	for i < n {
		j := i
		for j < n && ans[j] == ans[i] {
			j++
		}
		if j-i < 3 {
			return ""
		}
		i = j
	}
	return string(ans)
}
