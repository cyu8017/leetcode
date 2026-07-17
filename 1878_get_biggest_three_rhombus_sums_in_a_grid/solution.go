// LeetCode 1878 - Get Biggest Three Rhombus Sums in a Grid
// https://leetcode.com/problems/get-biggest-three-rhombus-sums-in-a-grid/

import "sort"

func getBiggestThree(grid [][]int) []int {
	m, n := len(grid), len(grid[0])
	s1 := make([][]int, m+2)
	s2 := make([][]int, m+2)
	for i := range s1 {
		s1[i] = make([]int, n+2)
		s2[i] = make([]int, n+2)
	}

	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			value := grid[i-1][j-1]
			s1[i][j] = s1[i-1][j-1] + value
			s2[i][j] = s2[i-1][j+1] + value
		}
	}

	rhombusSums := make(map[int]struct{})
	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			value := grid[i-1][j-1]
			limit := i - 1
			if m-i < limit {
				limit = m - i
			}
			if j-1 < limit {
				limit = j - 1
			}
			if n-j < limit {
				limit = n - j
			}
			rhombusSums[value] = struct{}{}
			for k := 1; k <= limit; k++ {
				a := s1[i+k][j] - s1[i][j-k]
				b := s1[i][j+k] - s1[i-k][j]
				c := s2[i][j-k] - s2[i-k][j]
				d := s2[i+k][j] - s2[i][j+k]
				sum := a + b + c + d - grid[i+k-1][j-1] + grid[i-k-1][j-1]
				rhombusSums[sum] = struct{}{}
			}
		}
	}

	values := make([]int, 0, len(rhombusSums))
	for value := range rhombusSums {
		values = append(values, value)
	}
	sort.Slice(values, func(i, j int) bool {
		return values[i] > values[j]
	})
	if len(values) > 3 {
		values = values[:3]
	}
	return values
}
