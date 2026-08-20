// LeetCode 0942 - DI String Match
// https://leetcode.com/problems/di-string-match/

func diStringMatch(s string) []int {
	lo, hi := 0, len(s)
	ans := make([]int, 0, len(s)+1)
	for _, ch := range s {
		if ch == 'I' {
			ans = append(ans, lo)
			lo++
		} else {
			ans = append(ans, hi)
			hi--
		}
	}
	ans = append(ans, lo)
	return ans
}
