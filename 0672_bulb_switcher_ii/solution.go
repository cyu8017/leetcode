// LeetCode 0672 - Bulb Switcher II
// https://leetcode.com/problems/bulb-switcher-ii/

func flipLights(n int, presses int) int {
	if n > 3 {
		n = 3
	}
	if presses == 0 {
		return 1
	}
	if presses == 1 {
		return []int{2, 3, 4}[n-1]
	}
	if presses == 2 {
		return []int{2, 4, 7}[n-1]
	}
	return []int{2, 4, 8}[n-1]
}
