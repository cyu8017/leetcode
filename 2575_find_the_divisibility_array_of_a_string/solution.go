// LeetCode 2575 - Find the Divisibility Array of a String
// https://leetcode.com/problems/find-the-divisibility-array-of-a-string/


func divisibilityArray(word string, m int) []int {
	ans := make([]int, len(word))
	cur := 0
	for i := 0; i < len(word); i++ {
		cur = (cur*10 + int(word[i]-'0')) % m
		if cur == 0 {
			ans[i] = 1
		}
	}
	return ans
}
