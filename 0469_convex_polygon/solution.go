// LeetCode 0469 - Convex Polygon
// https://leetcode.com/problems/convex-polygon/

func isConvex(points [][]int) bool {
	direction := 0
	count := len(points)
	for index := 0; index < count; index++ {
		x1 := points[(index+1)%count][0] - points[index][0]
		y1 := points[(index+1)%count][1] - points[index][1]
		x2 := points[(index+2)%count][0] - points[(index+1)%count][0]
		y2 := points[(index+2)%count][1] - points[(index+1)%count][1]
		cross := int64(x1)*int64(y2) - int64(y1)*int64(x2)
		if cross == 0 {
			continue
		}
		current := 1
		if cross < 0 {
			current = -1
		}
		if direction == 0 {
			direction = current
		} else if direction != current {
			return false
		}
	}
	return true
}
