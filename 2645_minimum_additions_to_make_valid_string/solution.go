// LeetCode 2645 - Minimum Additions to Make Valid String
// https://leetcode.com/problems/minimum-additions-to-make-valid-string/


func addMinimum(word string) int {
	ans, expect := 0, 0
	for i := 0; i < len(word); {
		need := byte('a' + expect)
		if word[i] == need {
			i++
		} else {
			ans++
		}
		expect = (expect + 1) % 3
	}
	ans += (3 - expect) % 3
	return ans
}
