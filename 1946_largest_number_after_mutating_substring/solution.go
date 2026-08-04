// LeetCode 1946 - Largest Number After Mutating Substring
// https://leetcode.com/problems/largest-number-after-mutating-substring/

func maximumNumber(num string, change []int) string {
	chars := []byte(num)
	started := false
	for i, ch := range chars {
		d := int(ch - '0')
		mapped := change[d]
		if mapped > d {
			chars[i] = byte('0' + mapped)
			started = true
		} else if mapped < d && started {
			break
		}
	}
	return string(chars)
}
