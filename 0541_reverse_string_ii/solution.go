// LeetCode 0541 - Reverse String II
// https://leetcode.com/problems/reverse-string-ii/

func reverseStr(s string, k int) string {
	chars := []byte(s)
	for start := 0; start < len(chars); start += 2 * k {
		end := start + k - 1
		if end >= len(chars) {
			end = len(chars) - 1
		}
		for left, right := start, end; left < right; left, right = left+1, right-1 {
			chars[left], chars[right] = chars[right], chars[left]
		}
	}
	return string(chars)
}
