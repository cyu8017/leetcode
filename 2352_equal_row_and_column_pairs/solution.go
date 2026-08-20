// LeetCode 2352 - Equal Row and Column Pairs
// https://leetcode.com/problems/equal-row-and-column-pairs/

func equalPairs(grid [][]int) int {
	n := len(grid)
	freq := map[string]int{}
	encode := func(arr []int) string {
		b := make([]byte, 0, n*4)
		for _, v := range arr {
			b = append(b, byte(v>>24), byte(v>>16), byte(v>>8), byte(v))
		}
		return string(b)
	}
	for i := 0; i < n; i++ {
		freq[encode(grid[i])]++
	}
	ans := 0
	col := make([]int, n)
	for j := 0; j < n; j++ {
		for i := 0; i < n; i++ {
			col[i] = grid[i][j]
		}
		ans += freq[encode(col)]
	}
	return ans
}
