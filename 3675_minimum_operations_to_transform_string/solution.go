// LeetCode 3675 - Minimum Operations to Transform String
// https://leetcode.com/problems/minimum-operations-to-transform-string/

func minOperations(s string) (ans int) {
	for _, c := range s {
		if c != 'a' {
			ans = max(ans, 26-int(c-'a'))
		}
	}
	return
}
