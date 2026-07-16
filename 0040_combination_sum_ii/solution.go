// LeetCode 0040 - Combination Sum II
// https://leetcode.com/problems/combination-sum-ii/

import "sort"

func combinationSum2(candidates []int, target int) [][]int {
	sort.Ints(candidates)
	result := make([][]int, 0)
	path := make([]int, 0)

	var backtrack func(start, remaining int)
	backtrack = func(start, remaining int) {
		if remaining == 0 {
			copyPath := append([]int(nil), path...)
			result = append(result, copyPath)
			return
		}
		if remaining < 0 {
			return
		}

		for i := start; i < len(candidates); i++ {
			if i > start && candidates[i] == candidates[i-1] {
				continue
			}
			path = append(path, candidates[i])
			backtrack(i+1, remaining-candidates[i])
			path = path[:len(path)-1]
		}
	}

	backtrack(0, target)
	return result
}
