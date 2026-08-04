// LeetCode 1240 - Tiling a Rectangle with the Fewest Squares
// https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/

func tilingRectangle(n int, m int) int {
	if n > m {
		n, m = m, n
	}
	heights := make([]int, m)
	best := n * m
	var search func(int)
	search = func(used int) {
		if used >= best {
			return
		}
		low := heights[0]
		for _, h := range heights[1:] {
			if h < low {
				low = h
			}
		}
		if low == n {
			best = used
			return
		}
		left := 0
		for left < m && heights[left] != low {
			left++
		}
		right := left
		for right < m && heights[right] == low {
			right++
		}
		maxSize := n - low
		if right-left < maxSize {
			maxSize = right - left
		}
		for size := maxSize; size >= 1; size-- {
			for i := left; i < left+size; i++ {
				heights[i] = low + size
			}
			search(used + 1)
			for i := left; i < left+size; i++ {
				heights[i] = low
			}
		}
	}
	search(0)
	return best
}
