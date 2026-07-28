// LeetCode 1066 - Campus Bikes II
// https://leetcode.com/problems/campus-bikes-ii/

func assignBikes(workers [][]int, bikes [][]int) int {
	m := len(bikes)
	memo := map[[2]int]int{}
	var dp func(i, mask int) int
	dp = func(i, mask int) int {
		if i == len(workers) {
			return 0
		}
		key := [2]int{i, mask}
		if v, ok := memo[key]; ok {
			return v
		}
		best := int(^uint(0) >> 1)
		wx, wy := workers[i][0], workers[i][1]
		for b := 0; b < m; b++ {
			if mask&(1<<b) != 0 {
				continue
			}
			bx, by := bikes[b][0], bikes[b][1]
			dist := abs1066(wx-bx) + abs1066(wy-by)
			cand := dist + dp(i+1, mask|(1<<b))
			if cand < best {
				best = cand
			}
		}
		memo[key] = best
		return best
	}
	return dp(0, 0)
}

func abs1066(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
