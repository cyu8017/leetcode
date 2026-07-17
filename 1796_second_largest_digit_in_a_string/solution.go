// LeetCode 1796 - Second Largest Digit in a String
// https://leetcode.com/problems/second-largest-digit-in-a-string/

func secondHighest(s string) int {
	largest := -1
	second := -1
	for i := 0; i < len(s); i++ {
		ch := s[i]
		if ch >= '0' && ch <= '9' {
			d := int(ch - '0')
			if d > largest {
				second = largest
				largest = d
			} else if d < largest && d > second {
				second = d
			}
		}
	}
	return second
}
