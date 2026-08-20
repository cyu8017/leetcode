// LeetCode 2282 - Number of People That Can Be Seen in a Grid
// https://leetcode.com/problems/number-of-people-that-can-be-seen-in-a-grid/

func seePeople(heights [][]int) [][]int {
	m, n := len(heights), len(heights[0])
	ans := make([][]int, m)
	for i := range ans {
		ans[i] = make([]int, n)
	}
	for i := 0; i < m; i++ {
		stack := []int{}
		for j := n - 1; j >= 0; j-- {
			cnt := 0
			for len(stack) > 0 && heights[i][stack[len(stack)-1]] < heights[i][j] {
				stack = stack[:len(stack)-1]
				cnt++
			}
			if len(stack) > 0 {
				cnt++
			}
			ans[i][j] += cnt
			for len(stack) > 0 && heights[i][stack[len(stack)-1]] == heights[i][j] {
				stack = stack[:len(stack)-1]
			}
			stack = append(stack, j)
		}
	}
	for j := 0; j < n; j++ {
		stack := []int{}
		for i := m - 1; i >= 0; i-- {
			cnt := 0
			for len(stack) > 0 && heights[stack[len(stack)-1]][j] < heights[i][j] {
				stack = stack[:len(stack)-1]
				cnt++
			}
			if len(stack) > 0 {
				cnt++
			}
			ans[i][j] += cnt
			for len(stack) > 0 && heights[stack[len(stack)-1]][j] == heights[i][j] {
				stack = stack[:len(stack)-1]
			}
			stack = append(stack, i)
		}
	}
	return ans
}
