// LeetCode 3996 - Even Number Of Knight Moves
// https://leetcode.com/problems/even-number-of-knight-moves/

func canReach(start []int, target []int) bool {
	return (start[0]+start[1])%2 == (target[0]+target[1])%2
}
