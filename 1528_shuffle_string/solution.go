// LeetCode 1528 - Shuffle String
// https://leetcode.com/problems/shuffle-string/

func restoreString(s string, indices []int) string {
	answer := make([]byte, len(s))
	for i, ch := range s {
		answer[indices[i]] = byte(ch)
	}
	return string(answer)
}
