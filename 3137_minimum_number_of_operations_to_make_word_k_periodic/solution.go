// LeetCode 3137 - Minimum Number of Operations to Make Word K-Periodic
// https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/

func minimumOperationsToMakeKPeriodic(word string, k int) int {
	cnt := map[string]int{}
	n := len(word)
	mx := 0
	for i := 0; i < n; i += k {
		s := word[i : i+k]
		cnt[s]++
		mx = max(mx, cnt[s])
	}
	return n/k - mx
}
