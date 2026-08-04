// LeetCode 1232 - Check If It Is a Straight Line
// https://leetcode.com/problems/check-if-it-is-a-straight-line/

func checkStraightLine(coordinates [][]int) bool {
	x0, y0 := coordinates[0][0], coordinates[0][1]
	dx, dy := coordinates[1][0]-x0, coordinates[1][1]-y0
	for _, p := range coordinates[2:] {
		if (p[0]-x0)*dy != (p[1]-y0)*dx {
			return false
		}
	}
	return true
}
