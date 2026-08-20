// LeetCode 0741 - Cherry Pickup
// https://leetcode.com/problems/cherry-pickup/

func cherryPickup(grid [][]int) int {
	n := len(grid)
	const neg = -1000000000
	memo := map[[3]int]int{}
	var dp func(r1, c1, c2 int) int
	dp = func(r1, c1, c2 int) int {
		r2 := r1 + c1 - c2
		if r1 >= n || c1 >= n || r2 >= n || c2 >= n || grid[r1][c1] == -1 || grid[r2][c2] == -1 {
			return neg
		}
		if r1 == n-1 && c1 == n-1 {
			return grid[r1][c1]
		}
		key := [3]int{r1, c1, c2}
		if v, ok := memo[key]; ok {
			return v
		}
		cherries := grid[r1][c1]
		if r1 != r2 || c1 != c2 {
			cherries += grid[r2][c2]
		}
		best := dp(r1+1, c1, c2)
		for _, cand := range []int{dp(r1, c1+1, c2), dp(r1+1, c1, c2+1), dp(r1, c1+1, c2+1)} {
			if cand > best {
				best = cand
			}
		}
		cherries += best
		memo[key] = cherries
		return cherries
	}
	ans := dp(0, 0, 0)
	if ans < 0 {
		return 0
	}
	return ans
}
