// LeetCode 1540 - Can Convert String in K Moves
// https://leetcode.com/problems/can-convert-string-in-k-moves/

func canConvertString(s string, t string, k int) bool {
	if len(s) != len(t) {
		return false
	}
	used := make([]int, 26)
	for i := 0; i < len(s); i++ {
		shift := (int(t[i]) - int(s[i]) + 26) % 26
		if shift == 0 {
			continue
		}
		used[shift]++
		if shift+26*(used[shift]-1) > k {
			return false
		}
	}
	return true
}
