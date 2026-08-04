// LeetCode 1119 - Remove Vowels from a String
// https://leetcode.com/problems/remove-vowels-from-a-string/

func removeVowels(s string) string {
	out := make([]byte, 0, len(s))
	for i := 0; i < len(s); i++ {
		ch := s[i]
		if ch != 'a' && ch != 'e' && ch != 'i' && ch != 'o' && ch != 'u' {
			out = append(out, ch)
		}
	}
	return string(out)
}
