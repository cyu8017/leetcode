// LeetCode 2844 - Minimum Operations to Make a Special Number
// https://leetcode.com/problems/minimum-operations-to-make-a-special-number/

func minimumOperations(num string) int {
	n := len(num)
	ans := n
	has0 := false
	for i := 0; i < n; i++ {
		if num[i] == '0' {
			has0 = true
		}
	}
	if has0 && n-1 < ans {
		ans = n - 1
	}
	targets := []string{"00", "25", "50", "75"}
	for _, t := range targets {
		j := n - 1
		for j >= 0 && num[j] != t[1] {
			j--
		}
		if j < 0 {
			continue
		}
		i := j - 1
		for i >= 0 && num[i] != t[0] {
			i--
		}
		if i < 0 {
			continue
		}
		cand := n - i - 2
		if cand < ans {
			ans = cand
		}
	}
	return ans
}
