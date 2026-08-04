// LeetCode 1963 - Minimum Number of Swaps to Make the String Balanced
// https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/

func minSwaps(s string) int {
	bal, mx := 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == '[' {
			bal++
		} else {
			bal--
		}
		if bal < mx {
			mx = bal
		}
	}
	return (-mx + 1) / 2
}
