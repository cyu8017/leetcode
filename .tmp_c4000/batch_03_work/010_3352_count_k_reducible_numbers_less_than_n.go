// LeetCode 3352 - Count K-Reducible Numbers Less Than N
// https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/

func countKReducibleNumbers(s string, k int) int {
	const mod = 1000000007
	// precompute reducible for popcounts
	red := make([]int, 801)
	red[1] = 0
	for i := 2; i <= 800; i++ {
		red[i] = 1 + red[bitsPop(i)]
	}
	n := len(s)
	memo := map[[3]int]int{}
	var dfs func(pos int, tight bool, ones int) int
	dfs = func(pos int, tight bool, ones int) int {
		if pos == n {
			if ones == 0 {
				return 0
			}
			if red[ones] <= k-1 {
				return 1
			}
			return 0
		}
		ti := 0
		if tight {
			ti = 1
		}
		key := [3]int{pos, ti, ones}
		if v, ok := memo[key]; ok {
			return v
		}
		up := 1
		if tight {
			up = int(s[pos] - '0')
		}
		ans := 0
		for d := 0; d <= up; d++ {
			nt := tight && d == up
			ans = (ans + dfs(pos+1, nt, ones+d)) % mod
		}
		memo[key] = ans
		return ans
	}
	return dfs(0, true, 0)
}

func bitsPop(x int) int {
	c := 0
	for x > 0 {
		c += x & 1
		x >>= 1
	}
	return c
}
