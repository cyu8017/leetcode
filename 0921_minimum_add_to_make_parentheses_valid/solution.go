// LeetCode 0921 - Minimum Add to Make Parentheses Valid
// https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

func minAddToMakeValid(s string) int {
	openNeed, closeNeed := 0, 0
	for _, ch := range s {
		if ch == '(' {
			closeNeed++
		} else if closeNeed > 0 {
			closeNeed--
		} else {
			openNeed++
		}
	}
	return openNeed + closeNeed
}
