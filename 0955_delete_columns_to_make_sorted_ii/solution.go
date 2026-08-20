// LeetCode 0955 - Delete Columns to Make Sorted II
// https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

func minDeletionSize(strs []string) int {
	n, m := len(strs), len(strs[0])
	sortedPair := make([]bool, n-1)
	deleted := 0
	for c := 0; c < m; c++ {
		needDelete := false
		for r := 0; r < n-1; r++ {
			if !sortedPair[r] && strs[r][c] > strs[r+1][c] {
				needDelete = true
				break
			}
		}
		if needDelete {
			deleted++
			continue
		}
		for r := 0; r < n-1; r++ {
			if strs[r][c] < strs[r+1][c] {
				sortedPair[r] = true
			}
		}
	}
	return deleted
}
