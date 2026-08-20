// LeetCode 0913 - Cat and Mouse
// https://leetcode.com/problems/cat-and-mouse/

func catMouseGame(graph [][]int) int {
	n := len(graph)
	const DRAW, MOUSE_WIN, CAT_WIN = 0, 1, 2
	states := make([][][]int, n)
	outDegree := make([][][]int, n)
	for cat := 0; cat < n; cat++ {
		states[cat] = make([][]int, n)
		outDegree[cat] = make([][]int, n)
		for mouse := 0; mouse < n; mouse++ {
			states[cat][mouse] = make([]int, 2)
			outDegree[cat][mouse] = make([]int, 2)
			outDegree[cat][mouse][0] = len(graph[mouse])
			cnt := 0
			for _, x := range graph[cat] {
				if x != 0 {
					cnt++
				}
			}
			outDegree[cat][mouse][1] = cnt
		}
	}
	type item struct{ cat, mouse, move, state int }
	queue := []item{}
	for cat := 1; cat < n; cat++ {
		for move := 0; move < 2; move++ {
			states[cat][0][move] = MOUSE_WIN
			queue = append(queue, item{cat, 0, move, MOUSE_WIN})
			states[cat][cat][move] = CAT_WIN
			queue = append(queue, item{cat, cat, move, CAT_WIN})
		}
	}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		cat, mouse, move, state := cur.cat, cur.mouse, cur.move, cur.state
		if cat == 2 && mouse == 1 && move == 0 {
			return state
		}
		prevMove := move ^ 1
		nodes := graph[mouse]
		if prevMove == 1 {
			nodes = graph[cat]
		}
		for _, prev := range nodes {
			prevCat, prevMouse := cat, mouse
			if prevMove == 1 {
				prevCat = prev
			} else {
				prevMouse = prev
			}
			if prevCat == 0 {
				continue
			}
			if states[prevCat][prevMouse][prevMove] != 0 {
				continue
			}
			if (prevMove == 0 && state == MOUSE_WIN) ||
				(prevMove == 1 && state == CAT_WIN) ||
				outDegree[prevCat][prevMouse][prevMove] == 1 {
				states[prevCat][prevMouse][prevMove] = state
				queue = append(queue, item{prevCat, prevMouse, prevMove, state})
			} else {
				outDegree[prevCat][prevMouse][prevMove]--
			}
		}
	}
	return states[2][1][0]
}
