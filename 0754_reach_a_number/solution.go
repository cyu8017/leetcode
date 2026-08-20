// LeetCode 0754 - Reach a Number
// https://leetcode.com/problems/reach-a-number/

func reachNumber(target int) int {
	if target < 0 {
		target = -target
	}
	steps, total := 0, 0
	for total < target || (total-target)%2 != 0 {
		steps++
		total += steps
	}
	return steps
}
