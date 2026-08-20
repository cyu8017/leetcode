// LeetCode 3258 - Count Substrings That Satisfy K-Constraint I
// https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/

func countKConstraintSubstrings(s string, k int) int {
	ans := 0
	n := len(s)
	for i := 0; i < n; i++ {
		z, o := 0, 0
		for j := i; j < n; j++ {
			if s[j] == '0' {
				z++
			} else {
				o++
			}
			if z <= k || o <= k {
				ans++
			} else {
				break
			}
		}
	}
	return ans
}
