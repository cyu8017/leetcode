// LeetCode 1698 - Number of Distinct Substrings in a String
// https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/

func countDistinct(s string) int {
	type trie map[byte]trie
	root := trie{}
	ans := 0
	for i := 0; i < len(s); i++ {
		node := root
		for j := i; j < len(s); j++ {
			c := s[j]
			if _, ok := node[c]; !ok {
				node[c] = trie{}
				ans++
			}
			node = node[c]
		}
	}
	return ans
}
