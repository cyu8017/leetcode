// LeetCode 0011 - Container With Most Water
// https://leetcode.com/problems/container-with-most-water/

func maxArea(height []int) int {
	left, right := 0, len(height)-1
	best := 0

	for left < right {
		width := right - left
		h := height[left]
		if height[right] < h {
			h = height[right]
		}
		if h*width > best {
			best = h * width
		}
		if height[left] < height[right] {
			left++
		} else {
			right--
		}
	}

	return best
}
