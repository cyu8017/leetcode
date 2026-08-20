// LeetCode 3227 - Vowels Game in a String
// https://leetcode.com/problems/vowels-game-in-a-string/

func doesAliceWin(s string) bool {
	vowels := "aeiou"
	for _, c := range s {
		if strings.ContainsRune(vowels, c) {
			return true
		}
	}
	return false
}
