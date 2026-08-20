// LeetCode 2801 - Count Stepping Numbers in Range
// https://leetcode.com/problems/count-stepping-numbers-in-range/

func countSteppingNumbers(low string, high string) int {
	const mod = 1_000_000_007
	var dfs func(s string, pos int, tight bool, last int, started bool, memo map[[4]int]int) int
	dfs = func(s string, pos int, tight bool, last int, started bool, memo map[[4]int]int) int {
		if pos == len(s) {
			if started {
				return 1
			}
			return 0
		}
		key := [4]int{pos, 0, last + 1, 0}
		if tight {
			key[1] = 1
		}
		if started {
			key[3] = 1
		}
		if v, ok := memo[key]; ok {
			return v
		}
		up := 9
		if tight {
			up = int(s[pos] - '0')
		}
		ans := 0
		for d := 0; d <= up; d++ {
			nt := tight && d == up
			if !started {
				if d == 0 {
					ans = (ans + dfs(s, pos+1, nt, -1, false, memo)) % mod
				} else {
					ans = (ans + dfs(s, pos+1, nt, d, true, memo)) % mod
				}
			} else if abs(d-last) == 1 {
				ans = (ans + dfs(s, pos+1, nt, d, true, memo)) % mod
			}
		}
		memo[key] = ans
		return ans
	}
	countTo := func(s string) int {
		return dfs(s, 0, true, -1, false, map[[4]int]int{})
	}
	dec := func(s string) string {
		b := []byte(s)
		i := len(b) - 1
		for i >= 0 && b[i] == '0' {
			b[i] = '9'
			i--
		}
		if i >= 0 {
			b[i]--
		}
		i = 0
		for i < len(b)-1 && b[i] == '0' {
			i++
		}
		return string(b[i:])
	}
	ans := countTo(high) - countTo(dec(low))
	ans %= mod
	if ans < 0 {
		ans += mod
	}
	return ans
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
