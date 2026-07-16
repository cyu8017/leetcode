// LeetCode 0039 - Combination Sum
// https://leetcode.com/problems/combination-sum/

func combinationSum(candidates []int, target int) [][]int {
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
			path = append(path, candidates[i])
			backtrack(i, remaining-candidates[i])
			path = path[:len(path)-1]
		}
	}

	backtrack(0, target)
	return result
}
