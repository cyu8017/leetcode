// LeetCode 0773 - Sliding Puzzle
// https://leetcode.com/problems/sliding-puzzle/

func slidingPuzzle(board [][]int) int {
	start := make([]byte, 0, 6)
	for _, row := range board {
		for _, cell := range row {
			start = append(start, byte('0'+cell))
		}
	}
	target := "123450"
	neighbors := [][]int{
		{1, 3},
		{0, 2, 4},
		{1, 5},
		{0, 4},
		{1, 3, 5},
		{2, 4},
	}
	type item struct {
		state string
		steps int
	}
	queue := []item{{string(start), 0}}
	seen := map[string]bool{string(start): true}
	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]
		if cur.state == target {
			return cur.steps
		}
		zero := 0
		for i := 0; i < 6; i++ {
			if cur.state[i] == '0' {
				zero = i
				break
			}
		}
		for _, nei := range neighbors[zero] {
			chars := []byte(cur.state)
			chars[zero], chars[nei] = chars[nei], chars[zero]
			nxt := string(chars)
			if !seen[nxt] {
				seen[nxt] = true
				queue = append(queue, item{nxt, cur.steps + 1})
			}
		}
	}
	return -1
}
