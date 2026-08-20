// LeetCode 2825 - Make String a Subsequence Using Cyclic Increments
// https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/

func canMakeSubsequence(str1 string, str2 string) bool {
	j := 0
	for i := 0; i < len(str1) && j < len(str2); i++ {
		a, b := str1[i], str2[j]
		if a == b || (a-'a'+1)%26 == int(b-'a') {
			j++
		}
	}
	return j == len(str2)
}
