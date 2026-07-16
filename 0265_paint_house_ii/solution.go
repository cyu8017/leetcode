// LeetCode 0265 - Paint House II
// https://leetcode.com/problems/paint-house-ii/

func minCostII(costs [][]int) int {
	if len(costs) == 0 {
		return 0
	}
	colorCount := len(costs[0])
	previous := append([]int(nil), costs[0]...)
	for row := 1; row < len(costs); row++ {
		minCost := previous[0]
		minIndex := 0
		for color := 1; color < colorCount; color++ {
			if previous[color] < minCost {
				minCost = previous[color]
				minIndex = color
			}
		}
		secondMin := int(^uint(0) >> 1)
		for color := 0; color < colorCount; color++ {
			if color != minIndex && previous[color] < secondMin {
				secondMin = previous[color]
			}
		}
		current := make([]int, colorCount)
		for color := 0; color < colorCount; color++ {
			extra := minCost
			if color == minIndex {
				extra = secondMin
			}
			current[color] = costs[row][color] + extra
		}
		previous = current
	}
	result := previous[0]
	for _, value := range previous[1:] {
		if value < result {
			result = value
		}
	}
	return result
}
