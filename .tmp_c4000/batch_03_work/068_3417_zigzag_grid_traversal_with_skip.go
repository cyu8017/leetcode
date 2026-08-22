// LeetCode 3417 - Zigzag Grid Traversal With Skip
// https://leetcode.com/problems/zigzag-grid-traversal-with-skip/

func zigzagTraversal(grid [][]int) []int {
	ans := []int{}
	skip := false
	for i, row := range grid {
		if i%2 == 0 {
			for _, v := range row {
				if !skip {
					ans = append(ans, v)
				}
				skip = !skip
			}
		} else {
			for j := len(row) - 1; j >= 0; j-- {
				if !skip {
					ans = append(ans, row[j])
				}
				skip = !skip
			}
		}
	}
	return ans
}
