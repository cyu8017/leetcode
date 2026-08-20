// LeetCode 0909 - Snakes and Ladders
// https://leetcode.com/problems/snakes-and-ladders/

func snakesAndLadders(board [][]int) int {
	n := len(board)
	pos := func(square int) (int, int) {
		square--
		row := square / n
		rem := square % n
		r := n - 1 - row
		c := rem
		if row%2 == 1 {
			c = n - 1 - rem
		}
		return r, c
	}
	target := n * n
	queue := []int{1}
	seen := map[int]bool{1: true}
	moves := 0
	for len(queue) > 0 {
		for sz := len(queue); sz > 0; sz-- {
			cur := queue[0]
			queue = queue[1:]
			if cur == target {
				return moves
			}
			hi := cur + 6
			if hi > target {
				hi = target
			}
			for nxt := cur + 1; nxt <= hi; nxt++ {
				r, c := pos(nxt)
				dest := nxt
				if board[r][c] != -1 {
					dest = board[r][c]
				}
				if !seen[dest] {
					seen[dest] = true
					queue = append(queue, dest)
				}
			}
		}
		moves++
	}
	return -1
}
