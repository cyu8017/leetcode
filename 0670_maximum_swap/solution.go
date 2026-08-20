// LeetCode 0670 - Maximum Swap
// https://leetcode.com/problems/maximum-swap/

import "strconv"

func maximumSwap(num int) int {
	digits := []byte(strconv.Itoa(num))
	last := map[int]int{}
	for i, d := range digits {
		last[int(d-'0')] = i
	}
	for i, ch := range digits {
		for candidate := 9; candidate > int(ch-'0'); candidate-- {
			j, ok := last[candidate]
			if ok && j > i {
				digits[i], digits[j] = digits[j], digits[i]
				v, _ := strconv.Atoi(string(digits))
				return v
			}
		}
	}
	return num
}
