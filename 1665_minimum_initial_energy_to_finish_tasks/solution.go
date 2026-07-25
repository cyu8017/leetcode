// LeetCode 1665 - Minimum Initial Energy to Finish Tasks
// https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

import "sort"

func minimumEffort(tasks [][]int) int {
	sort.Slice(tasks, func(i, j int) bool {
		return tasks[i][1]-tasks[i][0] > tasks[j][1]-tasks[j][0]
	})
	energy, spent := 0, 0
	for _, t := range tasks {
		cost, minimum := t[0], t[1]
		if spent+minimum > energy {
			energy = spent + minimum
		}
		spent += cost
	}
	return energy
}
