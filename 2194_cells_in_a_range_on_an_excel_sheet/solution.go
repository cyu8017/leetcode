// LeetCode 2194 - Cells in a Range on an Excel Sheet
// https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

func cellsInRange(s string) []string {
	ans := []string{}
	for c := s[0]; c <= s[3]; c++ {
		for r := s[1]; r <= s[4]; r++ {
			ans = append(ans, string([]byte{c, r}))
		}
	}
	return ans
}
