// LeetCode 3923 - Minimum Generations to Target Point
// https://leetcode.com/problems/minimum-generations-to-target-point/

func minGenerations(points [][]int, target []int) int {
	type point [3]int
	targetPoint := point{target[0], target[1], target[2]}
	generation := make(map[point]int)
	all := make([]point, 0, 343)
	for _, values := range points {
		p := point{values[0], values[1], values[2]}
		generation[p] = 0
		all = append(all, p)
	}
	if value, exists := generation[targetPoint]; exists {
		return value
	}

	for current := 1; ; current++ {
		limit := len(all)
		added := make([]point, 0)
		for i := 0; i < limit; i++ {
			for j := i + 1; j < limit; j++ {
				if all[i] == all[j] {
					continue
				}
				p := point{
					(all[i][0] + all[j][0]) / 2,
					(all[i][1] + all[j][1]) / 2,
					(all[i][2] + all[j][2]) / 2,
				}
				if _, exists := generation[p]; !exists {
					generation[p] = current
					added = append(added, p)
				}
			}
		}
		if value, exists := generation[targetPoint]; exists {
			return value
		}
		if len(added) == 0 {
			return -1
		}
		all = append(all, added...)
	}
}