// LeetCode 1779 - Find Nearest Point That Has the Same X or Y Coordinate
// https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

func nearestValidPoint(x int, y int, points [][]int) int {
	abs := func(v int) int {
		if v < 0 {
			return -v
		}
		return v
	}
	best := int(^uint(0) >> 1)
	ans := -1
	for i, point := range points {
		px, py := point[0], point[1]
		if px != x && py != y {
			continue
		}
		dist := abs(px-x) + abs(py-y)
		if dist < best {
			best = dist
			ans = i
		}
	}
	return ans
}
