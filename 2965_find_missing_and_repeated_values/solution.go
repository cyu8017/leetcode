// LeetCode 2965 - Find Missing and Repeated Values
// https://leetcode.com/problems/find-missing-and-repeated-values/

func findMissingAndRepeatedValues(grid [][]int) []int {
	n := len(grid)
	freq := make([]int, n*n+1)
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			freq[grid[i][j]]++
		}
	}
	rep, miss := 0, 0
	for i := 1; i <= n*n; i++ {
		if freq[i] == 2 {
			rep = i
		}
		if freq[i] == 0 {
			miss = i
		}
	}
	return []int{rep, miss}
}
