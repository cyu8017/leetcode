// LeetCode 0186 - Reverse Words in a String II
// https://leetcode.com/problems/reverse-words-in-a-string-ii/

func reverseWords(s []byte) {
	reverse := func(left, right int) {
		for left < right {
			s[left], s[right] = s[right], s[left]
			left++
			right--
		}
	}

	reverse(0, len(s)-1)
	start := 0
	for end := 0; end <= len(s); end++ {
		if end == len(s) || s[end] == ' ' {
			reverse(start, end-1)
			start = end + 1
		}
	}
}