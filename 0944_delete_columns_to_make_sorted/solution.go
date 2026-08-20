// LeetCode 0944 - Delete Columns to Make Sorted
// https://leetcode.com/problems/delete-columns-to-make-sorted/

func minDeletionSize(strs []string) int {
	ans := 0
	cols := len(strs[0])
	for c := 0; c < cols; c++ {
		for r := 0; r < len(strs)-1; r++ {
			if strs[r][c] > strs[r+1][c] {
				ans++
				break
			}
		}
	}
	return ans
}
