// LeetCode 0390 - Elimination Game
// https://leetcode.com/problems/elimination-game/

func lastRemaining(n int) int {
	left := 1
	right := n
	step := 1
	remaining := n
	fromLeft := true

	for left < right {
		if fromLeft || remaining%2 == 1 {
			left += step
		}
		right -= step
		step *= 2
		remaining /= 2
		fromLeft = !fromLeft
	}

	return left
}
