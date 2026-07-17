// LeetCode 1881 - Maximum Value after Insertion
// https://leetcode.com/problems/maximum-value-after-insertion/

import "strconv"

func maxValue(n string, x int) string {
	neg := n[0] == '-'
	start := 0
	if neg {
		start = 1
	}
	xStr := strconv.Itoa(x)
	for i := start; i < len(n); i++ {
		d, _ := strconv.Atoi(string(n[i]))
		if neg {
			if d > x {
				return n[:i] + xStr + n[i:]
			}
		} else if d < x {
			return n[:i] + xStr + n[i:]
		}
	}
	return n + xStr
}
