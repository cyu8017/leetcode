// LeetCode 1197 - Minimum Knight Moves
// https://leetcode.com/problems/minimum-knight-moves/

func minKnightMoves(x int, y int) int {
	if x < 0 {
		x = -x
	}
	if y < 0 {
		y = -y
	}
	memo := map[[2]int]int{}
	var dfs func(int, int) int
	dfs = func(a, b int) int {
		if a < b {
			a, b = b, a
		}
		key := [2]int{a, b}
		if v, ok := memo[key]; ok {
			return v
		}
		if a+b == 0 {
			return 0
		}
		if a+b == 2 {
			return 2
		}
		v := dfs(abs(a-1), abs(b-2))
		w := dfs(abs(a-2), abs(b-1))
		if w < v {
			v = w
		}
		memo[key] = v + 1
		return v + 1
	}
	return dfs(x, y)
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
