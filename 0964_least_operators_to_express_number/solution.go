// LeetCode 0964 - Least Operators to Express Number
// https://leetcode.com/problems/least-operators-to-express-number/

func leastOpsExpressTarget(x int, target int) int {
	memo := map[int]int{}
	var dfs func(int) int
	dfs = func(t int) int {
		if v, ok := memo[t]; ok {
			return v
		}
		if x > t {
			a := 2*t - 1
			b := 2 * (x - t)
			if a < b {
				memo[t] = a
			} else {
				memo[t] = b
			}
			return memo[t]
		}
		if x == t {
			memo[t] = 0
			return 0
		}
		prod := x
		n := 0
		for prod < t {
			prod *= x
			n++
		}
		if prod == t {
			memo[t] = n
			return n
		}
		ans := dfs(t-prod/x) + n
		if prod < 2*t {
			cand := dfs(prod-t) + n + 1
			if cand < ans {
				ans = cand
			}
		}
		memo[t] = ans
		return ans
	}
	return dfs(target)
}
