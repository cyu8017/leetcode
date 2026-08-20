// LeetCode 2718 - Sum of Matrix After Queries
// https://leetcode.com/problems/sum-of-matrix-after-queries/


func matrixSumQueries(n int, queries [][]int) int64 {
	rowSet, colSet := map[int]bool{}, map[int]bool{}
	var ans int64
	for i := len(queries) - 1; i >= 0; i-- {
		t, idx, v := queries[i][0], queries[i][1], queries[i][2]
		if t == 0 {
			if rowSet[idx] {
				continue
			}
			rowSet[idx] = true
			ans += int64(v) * int64(n-len(colSet))
		} else {
			if colSet[idx] {
				continue
			}
			colSet[idx] = true
			ans += int64(v) * int64(n-len(rowSet))
		}
	}
	return ans
}
