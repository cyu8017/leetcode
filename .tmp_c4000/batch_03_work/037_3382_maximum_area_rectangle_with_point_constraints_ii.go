// LeetCode 3382 - Maximum Area Rectangle With Point Constraints II
// https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-ii/

func maxRectangleArea(xCoord []int, yCoord []int) int64 {
	n := len(xCoord)
	points := make([][]int, n)
	for i := 0; i < n; i++ {
		points[i] = []int{xCoord[i], yCoord[i]}
	}
	set := map[[2]int]bool{}
	for _, p := range points {
		set[[2]int{p[0], p[1]}] = true
	}
	var ans int64 = -1
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			x1, y1 := points[i][0], points[i][1]
			x2, y2 := points[j][0], points[j][1]
			if x1 == x2 || y1 == y2 {
				continue
			}
			if !set[[2]int{x1, y2}] || !set[[2]int{x2, y1}] {
				continue
			}
			minX, maxX := x1, x2
			if minX > maxX {
				minX, maxX = maxX, minX
			}
			minY, maxY := y1, y2
			if minY > maxY {
				minY, maxY = maxY, minY
			}
			ok := true
			for _, p := range points {
				x, y := p[0], p[1]
				if x > minX && x < maxX && y > minY && y < maxY {
					ok = false
					break
				}
				onBorder := ((x == minX || x == maxX) && y >= minY && y <= maxY) || ((y == minY || y == maxY) && x >= minX && x <= maxX)
				if onBorder {
					isCorner := (x == minX || x == maxX) && (y == minY || y == maxY)
					if !isCorner {
						ok = false
						break
					}
				}
			}
			if ok {
				area := int64(maxX-minX) * int64(maxY-minY)
				if area > ans {
					ans = area
				}
			}
		}
	}
	return ans
}
