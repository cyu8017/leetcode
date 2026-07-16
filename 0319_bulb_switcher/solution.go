// LeetCode 0319 - Bulb Switcher
// https://leetcode.com/problems/bulb-switcher/

import "math"

func bulbSwitch(n int) int {
	return int(math.Sqrt(float64(n)))
}
