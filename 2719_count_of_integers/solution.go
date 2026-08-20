// LeetCode 2719 - Count of Integers
// https://leetcode.com/problems/count-of-integers/


func count(num1 string, num2 string, min_sum int, max_sum int) int {
	const MOD = 1000000007
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
		j := 0
		for j < len(b)-1 && b[j] == '0' {
			j++
		}
		return string(b[j:])
	}
	var dp func(string) int
	dp = func(s string) int {
		n := len(s)
		memo := map[[3]int]int{}
		var dfs func(pos int, sum int, tight bool) int
		dfs = func(pos, sum int, tight bool) int {
			if sum > max_sum {
				return 0
			}
			if pos == n {
				if sum >= min_sum {
					return 1
				}
				return 0
			}
			key := [3]int{pos, sum, 0}
			if tight {
				key[2] = 1
			}
			if v, ok := memo[key]; ok {
				return v
			}
			up := 9
			if tight {
				up = int(s[pos] - '0')
			}
			res := 0
			for d := 0; d <= up; d++ {
				res = (res + dfs(pos+1, sum+d, tight && d == up)) % MOD
			}
			memo[key] = res
			return res
		}
		return dfs(0, 0, true)
	}
	ans := (dp(num2) - dp(dec(num1)) + MOD) % MOD
	return ans
}
