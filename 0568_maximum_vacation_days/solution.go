// LeetCode 0568 - Maximum Vacation Days
// https://leetcode.com/problems/maximum-vacation-days/

func maxVacationDays(flights [][]int, days [][]int) int {
	cities := len(flights)
	weeks := len(days[0])
	const neg = -1_000_000_000
	dp := make([]int, cities)
	for i := range dp {
		dp[i] = neg
	}
	dp[0] = 0

	for week := 0; week < weeks; week++ {
		nxt := make([]int, cities)
		for i := range nxt {
			nxt[i] = neg
		}
		for city := 0; city < cities; city++ {
			if dp[city] == neg {
				continue
			}
			for dest := 0; dest < cities; dest++ {
				if dest == city || flights[city][dest] == 1 {
					val := dp[city] + days[dest][week]
					if val > nxt[dest] {
						nxt[dest] = val
					}
				}
			}
		}
		dp = nxt
	}

	best := neg
	for _, v := range dp {
		if v > best {
			best = v
		}
	}
	return best
}
