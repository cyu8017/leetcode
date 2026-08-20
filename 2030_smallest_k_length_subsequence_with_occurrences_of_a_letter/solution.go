// LeetCode 2030 - Smallest K-Length Subsequence With Occurrences of a Letter
// https://leetcode.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter/

func smallestSubsequence(s string, k int, letter byte, repetition int) string {
	n := len(s)
	remainLetter := 0
	for i := 0; i < n; i++ {
		if s[i] == letter {
			remainLetter++
		}
	}
	stack := []byte{}
	inStackLetter := 0
	for i := 0; i < n; i++ {
		ch := s[i]
		for len(stack) > 0 && ch < stack[len(stack)-1] && len(stack)+n-i > k {
			top := stack[len(stack)-1]
			if top == letter {
				if inStackLetter+remainLetter-1 < repetition {
					break
				}
				inStackLetter--
			}
			stack = stack[:len(stack)-1]
		}
		if len(stack) < k {
			if ch == letter {
				stack = append(stack, ch)
				inStackLetter++
			} else if k-len(stack) > repetition-inStackLetter {
				stack = append(stack, ch)
			}
		}
		if ch == letter {
			remainLetter--
		}
	}
	return string(stack)
}
