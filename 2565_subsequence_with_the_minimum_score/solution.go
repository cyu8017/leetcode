// LeetCode 2565 - Subsequence With the Minimum Score
// https://leetcode.com/problems/subsequence-with-the-minimum-score/


func minimumScore(s string, t string) int {
	n, m := len(s), len(t)
	left := make([]int, m)
	right := make([]int, m)
	for i := range left {
		left[i], right[i] = -1, -1
	}
	j := 0
	for i := 0; i < n && j < m; i++ {
		if s[i] == t[j] {
			left[j] = i
			j++
		}
	}
	j = m - 1
	for i := n - 1; i >= 0 && j >= 0; i-- {
		if s[i] == t[j] {
			right[j] = i
			j--
		}
	}
	if left[m-1] != -1 {
		return 0
	}
	ans := m
	// remove prefix
	for i := 0; i < m; i++ {
		if right[i] != -1 {
			if i < ans {
				ans = i
			}
			break
		}
	}
	// remove suffix
	for i := m - 1; i >= 0; i-- {
		if left[i] != -1 {
			if m-1-i < ans {
				ans = m - 1 - i
			}
			break
		}
	}
	j = 0
	for i := 0; i < m; i++ {
		if left[i] == -1 {
			break
		}
		for j < m && (right[j] == -1 || right[j] <= left[i]) {
			j++
		}
		if j < m {
			rem := j - i - 1
			if rem < ans {
				ans = rem
			}
		}
	}
	return ans
}
