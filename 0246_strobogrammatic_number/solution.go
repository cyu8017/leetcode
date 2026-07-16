// LeetCode 0246 - Strobogrammatic Number
// https://leetcode.com/problems/strobogrammatic-number/

func isStrobogrammatic(num string) bool {
	mapping := map[byte]byte{'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
	left := 0
	right := len(num) - 1
	for left <= right {
		if mapping[num[left]] != num[right] {
			return false
		}
		left++
		right--
	}
	return true
}
