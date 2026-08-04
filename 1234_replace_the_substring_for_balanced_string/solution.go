// LeetCode 1234 - Replace the Substring for Balanced String
// https://leetcode.com/problems/replace-the-substring-for-balanced-string/

func balancedString(s string) int {
	count := map[byte]int{}
	for i := 0; i < len(s); i++ {
		count[s[i]]++
	}
	limit := len(s) / 4
	n := len(s)
	left, answer := 0, n
	ok := func() bool {
		for _, c := range []byte{'Q', 'W', 'E', 'R'} {
			if count[c] > limit {
				return false
			}
		}
		return true
	}
	for right := 0; right < n; right++ {
		count[s[right]]--
		for left < n && ok() {
			if right-left+1 < answer {
				answer = right - left + 1
			}
			count[s[left]]++
			left++
		}
	}
	return answer
}
