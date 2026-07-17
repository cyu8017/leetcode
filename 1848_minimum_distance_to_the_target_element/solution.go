// LeetCode 1848 - Minimum Distance to the Target Element
// https://leetcode.com/problems/minimum-distance-to-the-target-element/

func getMinDistance(nums []int, target int, start int) int {
	best := len(nums)
	for i, value := range nums {
		if value == target {
			dist := i - start
			if dist < 0 {
				dist = -dist
			}
			if dist < best {
				best = dist
			}
		}
	}
	return best
}
