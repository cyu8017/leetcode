// LeetCode 1935 - Maximum Number of Words You Can Type
// https://leetcode.com/problems/maximum-number-of-words-you-can-type/

func canBeTypedWords(text string, brokenLetters string) int {
	broken := make([]bool, 26)
	for i := 0; i < len(brokenLetters); i++ {
		broken[brokenLetters[i]-'a'] = true
	}
	ans := 0
	ok := true
	for i := 0; i <= len(text); i++ {
		if i == len(text) || text[i] == ' ' {
			if ok {
				ans++
			}
			ok = true
		} else if broken[text[i]-'a'] {
			ok = false
		}
	}
	return ans
}
