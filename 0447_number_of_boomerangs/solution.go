// LeetCode 0447 - Number of Boomerangs
// https://leetcode.com/problems/number-of-boomerangs/

func numberOfBoomerangs(points [][]int) int {
	total := 0
	for _, anchor := range points {
		distances := make(map[int64]int)
		for _, other := range points {
			dx := int64(anchor[0] - other[0])
			dy := int64(anchor[1] - other[1])
			distances[dx*dx+dy*dy]++
		}
		for _, count := range distances {
			total += count * (count - 1)
		}
	}
	return total
}
