// LeetCode 0517 - Super Washing Machines
// https://leetcode.com/problems/super-washing-machines/

func findMinMoves(machines []int) int {
	total := 0
	for _, clothes := range machines {
		total += clothes
	}
	count := len(machines)
	if total%count != 0 {
		return -1
	}
	target := total / count
	prefix := 0
	result := 0
	for _, clothes := range machines {
		diff := clothes - target
		prefix += diff
		if abs(prefix) > result {
			result = abs(prefix)
		}
		if abs(diff) > result {
			result = abs(diff)
		}
	}
	return result
}

func abs(value int) int {
	if value < 0 {
		return -value
	}
	return value
}
