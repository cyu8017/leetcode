// LeetCode 1210 - Minimum Moves to Reach Target with Rotations
// https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/

func minimumMoves(grid [][]int) int {
	n := len(grid)
	type state struct{ r, c, orient int }
	start, target := state{0, 0, 0}, state{n - 1, n - 2, 0}
	type item struct {
		s     state
		moves int
	}
	q := []item{{start, 0}}
	seen := map[state]bool{start: true}
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		if cur.s == target {
			return cur.moves
		}
		r, c, orient := cur.s.r, cur.s.c, cur.s.orient
		nxt := []state{}
		if orient == 0 {
			if c+2 < n && grid[r][c+2] == 0 {
				nxt = append(nxt, state{r, c + 1, 0})
			}
			if r+1 < n && grid[r+1][c] == 0 && grid[r+1][c+1] == 0 {
				nxt = append(nxt, state{r + 1, c, 0}, state{r, c, 1})
			}
		} else {
			if r+2 < n && grid[r+2][c] == 0 {
				nxt = append(nxt, state{r + 1, c, 1})
			}
			if c+1 < n && grid[r][c+1] == 0 && grid[r+1][c+1] == 0 {
				nxt = append(nxt, state{r, c + 1, 1}, state{r, c, 0})
			}
		}
		for _, st := range nxt {
			if !seen[st] {
				seen[st] = true
				q = append(q, item{st, cur.moves + 1})
			}
		}
	}
	return -1
}
