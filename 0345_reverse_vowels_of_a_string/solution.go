// LeetCode 0345 - Reverse Vowels of a String
// https://leetcode.com/problems/reverse-vowels-of-a-string/

func reverseVowels(s string) string {
	vowels := map[byte]bool{
		'a': true, 'e': true, 'i': true, 'o': true, 'u': true,
		'A': true, 'E': true, 'I': true, 'O': true, 'U': true,
	}
	chars := []byte(s)
	left := 0
	right := len(chars) - 1

	for left < right {
		for left < right && !vowels[chars[left]] {
			left++
		}
		for left < right && !vowels[chars[right]] {
			right--
		}
		chars[left], chars[right] = chars[right], chars[left]
		left++
		right--
	}

	return string(chars)
}
