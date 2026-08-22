// LeetCode 3403 - Find the Lexicographically Largest String From the Box I
// https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/

func answerString(word string, numFriends int) string {
	if numFriends == 1 {
		return word
	}
	n := len(word)
	maxLen := n - (numFriends - 1)
	ans := ""
	for i := 0; i < n; i++ {
		end := i + maxLen
		if end > n {
			end = n
		}
		cand := word[i:end]
		if cand > ans {
			ans = cand
		}
	}
	return ans
}
