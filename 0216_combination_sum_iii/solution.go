// LeetCode 0216 - Combination Sum III
// https://leetcode.com/problems/combination-sum-iii/

func combinationSum3(k int, n int) [][]int {
	result := make([][]int, 0)
	path := make([]int, 0)

	var backtrack func(start, remaining int)
	backtrack = func(start, remaining int) {
		if len(path) == k {
			if remaining == 0 {
				copyPath := append([]int(nil), path...)
				result = append(result, copyPath)
			}
			return
		}
		if remaining <= 0 || len(path) >= k {
			return
		}

		for num := start; num <= 9; num++ {
			if num > remaining {
				break
			}
			path = append(path, num)
			backtrack(num+1, remaining-num)
			path = path[:len(path)-1]
		}
	}

	backtrack(1, n)
	return result
}
