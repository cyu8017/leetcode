// LeetCode 0467 - Unique Substrings in Wraparound String
// https://leetcode.com/problems/unique-substrings-in-wraparound-string/

func findSubstringInWraproundString(s string) int {
	counts := make([]int, 26)
	length := 0
	for index, char := range s {
		if index > 0 && (int(char-rune(s[index-1]))+26)%26 == 1 {
			length++
		} else {
			length = 1
		}
		position := int(char - 'a')
		if length > counts[position] {
			counts[position] = length
		}
	}
	total := 0
	for _, count := range counts {
		total += count
	}
	return total
}
