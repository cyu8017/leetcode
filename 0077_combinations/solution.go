// LeetCode 0077 - Combinations
// https://leetcode.com/problems/combinations/

func combine(n int, k int) [][]int {
	result := make([][]int, 0)
	path := make([]int, 0, k)

	var backtrack func(start int)
	backtrack = func(start int) {
		if len(path) == k {
			copyPath := append([]int(nil), path...)
			result = append(result, copyPath)
			return
		}

		remaining := k - len(path)
		for i := start; i <= n-remaining+1; i++ {
			path = append(path, i)
			backtrack(i + 1)
			path = path[:len(path)-1]
		}
	}

	backtrack(1)
	return result
}
