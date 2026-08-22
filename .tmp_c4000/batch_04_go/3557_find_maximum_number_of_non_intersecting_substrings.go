// LeetCode 3557 - Find Maximum Number of Non Intersecting Substrings
// https://leetcode.com/problems/find-maximum-number-of-non-intersecting-substrings/

func maxSubstrings(word string) int {
	ans := 0
	first := map[byte]int{}
	for i := 0; i < len(word); i++ {
		c := word[i]
		if _, ok := first[c]; !ok {
			first[c] = i
		} else if i-first[c]+1 >= 4 {
			ans++
			first = map[byte]int{}
		}
	}
	return ans
}
