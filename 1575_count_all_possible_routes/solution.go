// LeetCode 1575 - Count All Possible Routes
// https://leetcode.com/problems/count-all-possible-routes/

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func countRoutes(locations []int, start int, finish int, fuel int) int {
	const MOD = 1_000_000_007
	memo := map[[2]int]int{}
	var dp func(city, left int) int
	dp = func(city, left int) int {
		key := [2]int{city, left}
		if v, ok := memo[key]; ok {
			return v
		}
		total := 0
		if city == finish {
			total = 1
		}
		for nxt := 0; nxt < len(locations); nxt++ {
			cost := abs(locations[city] - locations[nxt])
			if nxt != city && cost <= left {
				total = (total + dp(nxt, left-cost)) % MOD
			}
		}
		memo[key] = total
		return total
	}
	return dp(start, fuel)
}
