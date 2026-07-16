// LeetCode 0401 - Binary Watch
// https://leetcode.com/problems/binary-watch/

import "fmt"

func readBinaryWatch(turnedOn int) []string {
	result := make([]string, 0)

	for hour := 0; hour < 12; hour++ {
		for minute := 0; minute < 60; minute++ {
			if bitsOn(hour)+bitsOn(minute) == turnedOn {
				result = append(result, fmt.Sprintf("%d:%02d", hour, minute))
			}
		}
	}

	return result
}

func bitsOn(value int) int {
	count := 0
	for value > 0 {
		count += value & 1
		value >>= 1
	}
	return count
}
