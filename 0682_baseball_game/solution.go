// LeetCode 0682 - Baseball Game
// https://leetcode.com/problems/baseball-game/

import "strconv"

func calPoints(ops []string) int {
	stack := []int{}
	for _, op := range ops {
		switch op {
		case "C":
			stack = stack[:len(stack)-1]
		case "D":
			stack = append(stack, stack[len(stack)-1]*2)
		case "+":
			stack = append(stack, stack[len(stack)-1]+stack[len(stack)-2])
		default:
			v, _ := strconv.Atoi(op)
			stack = append(stack, v)
		}
	}
	total := 0
	for _, v := range stack {
		total += v
	}
	return total
}
