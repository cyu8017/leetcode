// LeetCode 1521 - Find a Value of a Mysterious Function Closest to Target
// https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func closestToTarget(arr []int, target int) int {
	answer := int(1e9)
	current := map[int]bool{}
	for _, value := range arr {
		next := map[int]bool{value: true}
		for previous := range current {
			next[value&previous] = true
		}
		current = next
		for candidate := range current {
			d := abs(candidate - target)
			if d < answer {
				answer = d
			}
		}
	}
	return answer
}
