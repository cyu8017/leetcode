// LeetCode 2833 - Furthest Point From Origin
// https://leetcode.com/problems/furthest-point-from-origin/

func furthestDistanceFromOrigin(moves string) int {
	L, R, u := 0, 0, 0
	for i := 0; i < len(moves); i++ {
		switch moves[i] {
		case 'L':
			L++
		case 'R':
			R++
		default:
			u++
		}
	}
	d := L - R
	if d < 0 {
		d = -d
	}
	return d + u
}
