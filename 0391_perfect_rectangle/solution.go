// LeetCode 0391 - Perfect Rectangle
// https://leetcode.com/problems/perfect-rectangle/

func isRectangleCover(rectangles [][]int) bool {
	points := make(map[[2]int]int)
	var area int64
	minX, minY := int(1<<31-1), int(1<<31-1)
	maxX, maxY := int(-1<<31), int(-1<<31)

	for _, rect := range rectangles {
		x1, y1, x2, y2 := rect[0], rect[1], rect[2], rect[3]
		area += int64(x2-x1) * int64(y2-y1)
		if x1 < minX {
			minX = x1
		}
		if y1 < minY {
			minY = y1
		}
		if x2 > maxX {
			maxX = x2
		}
		if y2 > maxY {
			maxY = y2
		}

		for _, point := range [][2]int{{x1, y1}, {x1, y2}, {x2, y1}, {x2, y2}} {
			points[point] ^= 1
		}
	}

	if len(points) != 4 {
		return false
	}
	corners := [][2]int{{minX, minY}, {minX, maxY}, {maxX, minY}, {maxX, maxY}}
	for _, corner := range corners {
		if points[corner] != 1 {
			return false
		}
	}
	for _, count := range points {
		if count != 1 {
			return false
		}
	}

	return area == int64(maxX-minX)*int64(maxY-minY)
}
