// LeetCode 3256 - Maximum Value Sum by Placing Three Rooks I
// https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-i/

func maximumValueSum(board [][]int) int64 {
	m := len(board)
	n := len(board[0])
	type cell struct{ v, c int }
	tops := make([][]cell, m)
	for i := 0; i < m; i++ {
		row := make([]cell, 0, 3)
		for j := 0; j < n; j++ {
			cur := cell{board[i][j], j}
			placed := false
			for t := 0; t < len(row); t++ {
				if cur.v > row[t].v {
					row = append(row, cell{})
					copy(row[t+1:], row[t:])
					row[t] = cur
					placed = true
					break
				}
			}
			if !placed {
				row = append(row, cur)
			}
			if len(row) > 3 {
				row = row[:3]
			}
		}
		tops[i] = row
	}
	ans := int64(-1 << 62)
	for i := 0; i < m; i++ {
		for _, a := range tops[i] {
			for j := i + 1; j < m; j++ {
				for _, b := range tops[j] {
					if a.c == b.c {
						continue
					}
					for k := j + 1; k < m; k++ {
						for _, c := range tops[k] {
							if c.c == a.c || c.c == b.c {
								continue
							}
							s := int64(a.v) + int64(b.v) + int64(c.v)
							if s > ans {
								ans = s
							}
						}
					}
				}
			}
		}
	}
	return ans
}
