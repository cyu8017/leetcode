// LeetCode 1160 - Find Words That Can Be Formed by Characters
// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

func countCharacters(words []string, chars string) int {
	have := [26]int{}
	for i := 0; i < len(chars); i++ {
		have[chars[i]-'a']++
	}
	ans := 0
	for _, w := range words {
		need := [26]int{}
		ok := true
		for i := 0; i < len(w); i++ {
			need[w[i]-'a']++
			if need[w[i]-'a'] > have[w[i]-'a'] {
				ok = false
				break
			}
		}
		if ok {
			ans += len(w)
		}
	}
	return ans
}
