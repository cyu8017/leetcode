// LeetCode 3228 - Maximum Number of Operations to Move Ones to the End
// https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/

func maxOperations(s string) (ans int) {
	cnt := 0
	for i, c := range s {
		if c == '1' {
			cnt++
		} else if i > 0 && s[i-1] == '1' {
			ans += cnt
		}
	}
	return
}
