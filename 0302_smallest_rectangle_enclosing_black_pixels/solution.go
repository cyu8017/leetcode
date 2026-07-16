// LeetCode 0302 - Smallest Rectangle Enclosing Black Pixels
// https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/

func minArea(image [][]byte, x int, y int) int {
	rows := len(image)
	cols := len(image[0])

	columnHasBlack := func(col int) bool {
		for row := 0; row < rows; row++ {
			if image[row][col] == '1' {
				return true
			}
		}
		return false
	}

	rowHasBlack := func(row int) bool {
		for col := 0; col < cols; col++ {
			if image[row][col] == '1' {
				return true
			}
		}
		return false
	}

	left, right := 0, y
	for left < right {
		mid := left + (right-left)/2
		if columnHasBlack(mid) {
			right = mid
		} else {
			left = mid + 1
		}
	}
	leftBound := left

	left, right = y, cols-1
	for left < right {
		mid := left + (right-left+1)/2
		if columnHasBlack(mid) {
			left = mid
		} else {
			right = mid - 1
		}
	}
	rightBound := left

	top, bottom := 0, x
	for top < bottom {
		mid := top + (bottom-top)/2
		if rowHasBlack(mid) {
			bottom = mid
		} else {
			top = mid + 1
		}
	}
	topBound := top

	top, bottom = x, rows-1
	for top < bottom {
		mid := top + (bottom-top+1)/2
		if rowHasBlack(mid) {
			top = mid
		} else {
			bottom = mid - 1
		}
	}
	bottomBound := top

	return (rightBound - leftBound + 1) * (bottomBound - topBound + 1)
}
