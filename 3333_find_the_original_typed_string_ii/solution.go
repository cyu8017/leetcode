// LeetCode 3333 - Find the Original Typed String II
// https://leetcode.com/problems/find-the-original-typed-string-ii/

func possibleStringCount(word string, k int) int {
	const mod = 1000000007
	groups := []int{}
	for i := 0; i < len(word); {
		j := i
		for j < len(word) && word[j] == word[i] {
			j++
		}
		groups = append(groups, j-i)
		i = j
	}
	total := 1
	for _, g := range groups {
		total = total * g % mod
	}
	if k <= len(groups) {
		return total
	}
	// subtract strings with length < k
	// dp: number of ways to get exact length using groups (each group contributes 1..g)
	need := k - 1
	dp := make([]int, need)
	dp[0] = 1
	for _, g := range groups {
		ndp := make([]int, need)
		pref := make([]int, need+1)
		for i := 0; i < need; i++ {
			pref[i+1] = (pref[i] + dp[i]) % mod
		}
		for s := 0; s < need; s++ {
			// sum dp[s-1] + ... + dp[s-g] (take 1..g chars, at least 1)
			lo := s - g
			if lo < 0 {
				lo = 0
			}
			hi := s - 1
			if hi >= 0 {
				ndp[s] = (pref[hi+1] - pref[lo] + mod) % mod
			}
		}
		dp = ndp
	}
	bad := 0
	for _, v := range dp {
		bad = (bad + v) % mod
	}
	return (total - bad + mod) % mod
}
