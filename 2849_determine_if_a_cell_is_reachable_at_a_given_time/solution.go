// LeetCode 2849 - Determine if a Cell Is Reachable at a Given Time
// https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/

func isReachableAtTime(sx int, sy int, fx int, fy int, t int) bool {
	dx := sx - fx
	if dx < 0 {
		dx = -dx
	}
	dy := sy - fy
	if dy < 0 {
		dy = -dy
	}
	need := dx
	if dy > need {
		need = dy
	}
	if need == 0 {
		return t != 1
	}
	return t >= need
}
