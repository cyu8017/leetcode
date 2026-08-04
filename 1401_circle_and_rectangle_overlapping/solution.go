// LeetCode 1401 - Circle and Rectangle Overlapping
// https://leetcode.com/problems/circle-and-rectangle-overlapping/

func checkOverlap(radius int, xCenter int, yCenter int, x1 int, y1 int, x2 int, y2 int) bool {
	x := xCenter
	if x < x1 {
		x = x1
	} else if x > x2 {
		x = x2
	}
	y := yCenter
	if y < y1 {
		y = y1
	} else if y > y2 {
		y = y2
	}
	dx, dy := x-xCenter, y-yCenter
	return dx*dx+dy*dy <= radius*radius
}
