// LeetCode 3773 - Maximum Number Of Equal Length Runs
// https://leetcode.com/problems/maximum-number-of-equal-length-runs/

func maxSameLengthRuns(s string) (ans int) {
	cnt := map[int]int{}
	n := len(s)
	for i := 0; i < n; {
		j := i + 1
		for j < n && s[j] == s[i] {
			j++
		}
		m := j - i
		cnt[m]++
		ans = max(ans, cnt[m])
		i = j
	}
	return
}
