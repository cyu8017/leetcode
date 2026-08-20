// LeetCode 2027 - Minimum Moves to Convert String
// https://leetcode.com/problems/minimum-moves-to-convert-string/

func minimumMoves(s string) int {
	ans := 0
	for i := 0; i < len(s); {
		if s[i] == 'X' {
			ans++
			i += 3
		} else {
			i++
		}
	}
	return ans
}
