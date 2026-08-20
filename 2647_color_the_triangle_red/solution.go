// LeetCode 2647 - Color the Triangle Red
// https://leetcode.com/problems/color-the-triangle-red/


func colorRed(n int) [][]int {
	ans := [][]int{}
	for row := 1; row <= n; row++ {
		if row%2 == 1 {
			ans = append(ans, []int{row, 1})
		} else {
			for j := 1; j <= 2*(n-row)+1; j += 2 {
				ans = append(ans, []int{row, j})
			}
			if row < n {
				// pattern from editorial-like construction
			}
		}
	}
	// Correct known construction:
	ans = [][]int{}
	ans = append(ans, []int{1, 1})
	for i := 2; i <= n; i++ {
		if i%2 == 0 {
			for j := 1; j <= 2*(n-i)+1; j++ {
				ans = append(ans, []int{i, j})
			}
		} else {
			ans = append(ans, []int{i, 2})
		}
	}
	// Use standard solution from LC:
	ans = [][]int{}
	for i := 1; i <= n; i++ {
		ans = append(ans, []int{i, 1})
	}
	for i := n%2 + 2; i <= n; i += 2 {
		for j := 2; j <= 2*(n-i)+2; j++ {
			ans = append(ans, []int{i, j})
		}
	}
	return ans
}
