// LeetCode 0279 - Perfect Squares
// https://leetcode.com/problems/perfect-squares/

func numSquares(n int) int {
	squares := make([]int, 0)
	for value := 1; value*value <= n; value++ {
		squares = append(squares, value*value)
	}

	type state struct {
		remain int
		steps  int
	}
	queue := []state{{remain: n, steps: 0}}
	visited := map[int]bool{n: true}

	for len(queue) > 0 {
		current := queue[0]
		queue = queue[1:]
		if current.remain == 0 {
			return current.steps
		}
		for _, square := range squares {
			next := current.remain - square
			if next < 0 {
				break
			}
			if !visited[next] {
				visited[next] = true
				queue = append(queue, state{remain: next, steps: current.steps + 1})
			}
		}
	}
	return 0
}
