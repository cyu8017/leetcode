// LeetCode 1263 - Minimum Moves to Move a Box to Their Target Location
// https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/

func minPushBox(grid [][]byte) int {
	m, n := len(grid), len(grid[0])
	var box, player, target [2]int
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			switch grid[r][c] {
			case 'B':
				box = [2]int{r, c}
			case 'S':
				player = [2]int{r, c}
			case 'T':
				target = [2]int{r, c}
			}
		}
	}
	reachable := func(start, blocked [2]int) map[[2]int]bool {
		seen := map[[2]int]bool{start: true}
		stack := [][2]int{start}
		for len(stack) > 0 {
			cur := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			for _, d := range [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
				nxt := [2]int{cur[0] + d[0], cur[1] + d[1]}
				if nxt[0] >= 0 && nxt[0] < m && nxt[1] >= 0 && nxt[1] < n &&
					grid[nxt[0]][nxt[1]] != '#' && nxt != blocked && !seen[nxt] {
					seen[nxt] = true
					stack = append(stack, nxt)
				}
			}
		}
		return seen
	}
	type state struct {
		b, p [2]int
	}
	type item struct {
		b, p  [2]int
		push  int
	}
	q := []item{{box, player, 0}}
	seen := map[state]bool{{box, player}: true}
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		if cur.b == target {
			return cur.push
		}
		can := reachable(cur.p, cur.b)
		for _, d := range [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
			stand := [2]int{cur.b[0] - d[0], cur.b[1] - d[1]}
			nb := [2]int{cur.b[0] + d[0], cur.b[1] + d[1]}
			if can[stand] && nb[0] >= 0 && nb[0] < m && nb[1] >= 0 && nb[1] < n && grid[nb[0]][nb[1]] != '#' {
				st := state{nb, cur.b}
				if !seen[st] {
					seen[st] = true
					q = append(q, item{nb, cur.b, cur.push + 1})
				}
			}
		}
	}
	return -1
}
