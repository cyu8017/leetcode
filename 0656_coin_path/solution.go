// LeetCode 0656 - Coin Path
// https://leetcode.com/problems/coin-path/

func cheapestJump(coins []int, maxJump int) []int {
	n := len(coins)
	if coins[n-1] == -1 {
		return []int{}
	}
	const inf = int64(1e18)
	cost := make([]int64, n)
	nxt := make([]int, n)
	for i := range cost {
		cost[i] = inf
		nxt[i] = -1
	}
	cost[n-1] = int64(coins[n-1])
	for i := n - 2; i >= 0; i-- {
		if coins[i] == -1 {
			continue
		}
		for jump := 1; jump <= maxJump; jump++ {
			j := i + jump
			if j >= n {
				break
			}
			if cost[j] == inf {
				continue
			}
			candidate := int64(coins[i]) + cost[j]
			if candidate < cost[i] || (candidate == cost[i] && (nxt[i] == -1 || j < nxt[i])) {
				cost[i] = candidate
				nxt[i] = j
			}
		}
	}
	if cost[0] == inf {
		return []int{}
	}
	path := []int{1}
	i := 0
	for i != n-1 {
		i = nxt[i]
		path = append(path, i+1)
	}
	return path
}
