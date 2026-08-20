// LeetCode 0809 - Expressive Words
// https://leetcode.com/problems/expressive-words/

func expressiveWords(s string, words []string) int {
	groups := func(text string) [][2]int {
		result := [][2]int{}
		i := 0
		for i < len(text) {
			j := i
			for j < len(text) && text[j] == text[i] {
				j++
			}
			result = append(result, [2]int{int(text[i]), j - i})
			i = j
		}
		return result
	}
	target := groups(s)
	stretchy := func(word string) bool {
		source := groups(word)
		if len(source) != len(target) {
			return false
		}
		for i := range source {
			if source[i][0] != target[i][0] {
				return false
			}
			c1, c2 := source[i][1], target[i][1]
			if c1 > c2 || (c1 != c2 && c2 < 3) {
				return false
			}
		}
		return true
	}
	ans := 0
	for _, word := range words {
		if stretchy(word) {
			ans++
		}
	}
	return ans
}
