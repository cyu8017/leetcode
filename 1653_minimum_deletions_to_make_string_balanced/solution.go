// LeetCode 1653 - Minimum Deletions to Make String Balanced
// https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

func minimumDeletions(s string) int {
	b, ans := 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == 'b' {
			b++
		} else {
			if ans+1 < b {
				ans++
			} else {
				ans = b
			}
		}
	}
	return ans
}
