// LeetCode 1274 - Number of Ships in a Rectangle
// https://leetcode.com/problems/number-of-ships-in-a-rectangle/

type Point struct{ X, Y int }

type Sea interface {
	HasShips(topRight, bottomLeft Point) bool
}

func countShips(sea Sea, topRight Point, bottomLeft Point) int {
	tx, ty := topRight.X, topRight.Y
	bx, by := bottomLeft.X, bottomLeft.Y
	if tx < bx || ty < by || !sea.HasShips(topRight, bottomLeft) {
		return 0
	}
	if tx == bx && ty == by {
		return 1
	}
	mx, my := (tx+bx)/2, (ty+by)/2
	return countShips(sea, Point{mx, my}, Point{bx, by}) +
		countShips(sea, Point{tx, my}, Point{mx + 1, by}) +
		countShips(sea, Point{mx, ty}, Point{bx, my + 1}) +
		countShips(sea, Point{tx, ty}, Point{mx + 1, my + 1})
}
