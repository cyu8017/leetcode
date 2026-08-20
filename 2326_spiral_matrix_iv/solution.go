// LeetCode 2326 - Spiral Matrix IV
// https://leetcode.com/problems/spiral-matrix-iv/

type ListNode struct {
	Val  int
	Next *ListNode
}

func spiralMatrix(m int, n int, head *ListNode) [][]int {
	ans := make([][]int, m)
	for i := range ans {
		ans[i] = make([]int, n)
		for j := range ans[i] {
			ans[i][j] = -1
		}
	}
	dirs := [][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	r, c, d := 0, 0, 0
	for head != nil {
		ans[r][c] = head.Val
		head = head.Next
		nr, nc := r+dirs[d][0], c+dirs[d][1]
		if nr < 0 || nr >= m || nc < 0 || nc >= n || ans[nr][nc] != -1 {
			d = (d + 1) % 4
			nr, nc = r+dirs[d][0], c+dirs[d][1]
		}
		r, c = nr, nc
	}
	return ans
}
