// LeetCode 0755 - Pour Water
// https://leetcode.com/problems/pour-water/

func pourWater(heights []int, volume int, k int) []int {
	for v := 0; v < volume; v++ {
		index := k
		for i := k - 1; i >= 0; i-- {
			if heights[i] > heights[index] {
				break
			}
			if heights[i] < heights[index] {
				index = i
			}
		}
		if index != k {
			heights[index]++
			continue
		}
		index = k
		for i := k + 1; i < len(heights); i++ {
			if heights[i] > heights[index] {
				break
			}
			if heights[i] < heights[index] {
				index = i
			}
		}
		heights[index]++
	}
	return heights
}
