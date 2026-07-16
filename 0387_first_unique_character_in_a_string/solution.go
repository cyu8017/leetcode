// LeetCode 0387 - First Unique Character in a String
// https://leetcode.com/problems/first-unique-character-in-a-string/

func firstUniqChar(s string) int {
	counts := make([]int, 26)

	for _, ch := range s {
		counts[ch-'a']++
	}

	for index, ch := range s {
		if counts[ch-'a'] == 1 {
			return index
		}
	}

	return -1
}
