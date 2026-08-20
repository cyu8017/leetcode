// LeetCode 0636 - Exclusive Time of Functions
// https://leetcode.com/problems/exclusive-time-of-functions/

import (
	"strconv"
	"strings"
)

func exclusiveTime(n int, logs []string) []int {
	result := make([]int, n)
	stack := []int{}
	prevTime := 0
	for _, log := range logs {
		parts := strings.Split(log, ":")
		funcID, _ := strconv.Atoi(parts[0])
		time, _ := strconv.Atoi(parts[2])
		if parts[1] == "start" {
			if len(stack) > 0 {
				result[stack[len(stack)-1]] += time - prevTime
			}
			stack = append(stack, funcID)
			prevTime = time
		} else {
			result[stack[len(stack)-1]] += time - prevTime + 1
			stack = stack[:len(stack)-1]
			prevTime = time + 1
		}
	}
	return result
}
