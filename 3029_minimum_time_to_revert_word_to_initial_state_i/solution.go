// LeetCode 3029 - Minimum Time to Revert Word to Initial State I
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i/

func minimumTimeToInitialState(word string, k int) int {
	n := len(word)
	for i := k; i < n; i += k {
		if word[i:] == word[:n-i] {
			return i / k
		}
	}
	return (n + k - 1) / k
}
