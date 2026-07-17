// LeetCode 1725 - Number Of Rectangles That Can Form The Largest Square
// https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

func countGoodRectangles(rectangles [][]int) int {
	best := 0
	count := 0
	for _, rect := range rectangles {
		side := rect[0]
		if rect[1] < side {
			side = rect[1]
		}
		if side > best {
			best = side
			count = 1
		} else if side == best {
			count++
		}
	}
	return count
}
