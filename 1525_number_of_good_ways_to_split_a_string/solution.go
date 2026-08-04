// LeetCode 1525 - Number of Good Ways to Split a String
// https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

func numSplits(s string) int {
	right := map[byte]int{}
	for i := 0; i < len(s); i++ {
		right[s[i]]++
	}
	left := map[byte]bool{}
	answer := 0
	for i := 0; i < len(s)-1; i++ {
		ch := s[i]
		left[ch] = true
		right[ch]--
		if right[ch] == 0 {
			delete(right, ch)
		}
		if len(left) == len(right) {
			answer++
		}
	}
	return answer
}
