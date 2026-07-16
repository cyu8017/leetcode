// LeetCode 0254 - Factor Combinations
// https://leetcode.com/problems/factor-combinations/

func getFactors(n int) [][]int {
	result := make([][]int, 0)
	path := make([]int, 0)

	var backtrack func(remain, start int)
	backtrack = func(remain, start int) {
		if start > remain {
			if len(path) > 1 {
				copyPath := append([]int(nil), path...)
				result = append(result, copyPath)
			}
			return
		}

		for factor := start; factor*factor <= remain; factor++ {
			if remain%factor == 0 {
				path = append(path, factor)
				backtrack(remain/factor, factor)
				path = path[:len(path)-1]
			}
		}

		if len(path) > 0 {
			path = append(path, remain)
			if len(path) > 1 {
				copyPath := append([]int(nil), path...)
				result = append(result, copyPath)
			}
			path = path[:len(path)-1]
		}
	}

	backtrack(n, 2)
	return result
}
