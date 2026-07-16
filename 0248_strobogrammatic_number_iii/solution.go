// LeetCode 0248 - Strobogrammatic Number III
// https://leetcode.com/problems/strobogrammatic-number-iii/

import "strconv"

func strobogrammaticInRange(low string, high string) int {
	pairs := [][2]string{
		{"0", "0"},
		{"1", "1"},
		{"6", "9"},
		{"8", "8"},
		{"9", "6"},
	}

	var build func(left, right int) []string
	build = func(left, right int) []string {
		if left > right {
			return []string{""}
		}
		if left == right {
			return []string{"0", "1", "8"}
		}
		result := make([]string, 0)
		for _, pair := range pairs {
			start, end := pair[0], pair[1]
			if left == 0 && start == "0" {
				continue
			}
			for _, middle := range build(left+1, right-1) {
				result = append(result, start+middle+end)
			}
		}
		return result
	}

	lowValue, _ := strconv.ParseInt(low, 10, 64)
	highValue, _ := strconv.ParseInt(high, 10, 64)
	count := 0
	for length := len(low); length <= len(high); length++ {
		for _, value := range build(0, length-1) {
			numeric, _ := strconv.ParseInt(value, 10, 64)
			if lowValue <= numeric && numeric <= highValue {
				count++
			}
		}
	}
	return count
}
