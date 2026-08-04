// LeetCode 1536 - Minimum Swaps to Arrange a Binary Grid
// https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/

func minSwaps(grid [][]int) int {
	n := len(grid)
	zeros := make([]int, n)
	for i, row := range grid {
		count := 0
		for j := n - 1; j >= 0; j-- {
			if row[j] != 0 {
				break
			}
			count++
		}
		zeros[i] = count
	}
	answer := 0
	for i := 0; i < n; i++ {
		required := n - i - 1
		j := i
		for j < n && zeros[j] < required {
			j++
		}
		if j == n {
			return -1
		}
		answer += j - i
		val := zeros[j]
		copy(zeros[i+1:j+1], zeros[i:j])
		zeros[i] = val
	}
	return answer
}
