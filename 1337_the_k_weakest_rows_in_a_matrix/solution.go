// LeetCode 1337 - The K Weakest Rows in a Matrix
// https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

import "sort"

func kWeakestRows(mat [][]int, k int) []int {
	type pair struct{ soldiers, idx int }
	rows := make([]pair, len(mat))
	for i, row := range mat {
		s := 0
		for _, v := range row {
			s += v
		}
		rows[i] = pair{s, i}
	}
	sort.Slice(rows, func(i, j int) bool {
		if rows[i].soldiers != rows[j].soldiers {
			return rows[i].soldiers < rows[j].soldiers
		}
		return rows[i].idx < rows[j].idx
	})
	answer := make([]int, k)
	for i := 0; i < k; i++ {
		answer[i] = rows[i].idx
	}
	return answer
}
