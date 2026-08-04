// LeetCode 1284 - Minimum Number of Flips to Convert Binary Matrix to Zero Matrix
// https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/

func minFlips(mat [][]int) int {
	m, n := len(mat), len(mat[0])
	start := 0
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			start |= mat[r][c] << (r*n + c)
		}
	}
	masks := []int{}
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			mask := 0
			for _, d := range [][2]int{{0, 0}, {1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
				nr, nc := r+d[0], c+d[1]
				if nr >= 0 && nr < m && nc >= 0 && nc < n {
					mask ^= 1 << (nr*n + nc)
				}
			}
			masks = append(masks, mask)
		}
	}
	type item struct{ state, dist int }
	q := []item{{start, 0}}
	seen := map[int]bool{start: true}
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		if cur.state == 0 {
			return cur.dist
		}
		for _, mask := range masks {
			nxt := cur.state ^ mask
			if !seen[nxt] {
				seen[nxt] = true
				q = append(q, item{nxt, cur.dist + 1})
			}
		}
	}
	return -1
}
