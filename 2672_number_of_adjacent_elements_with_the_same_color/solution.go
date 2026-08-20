// LeetCode 2672 - Number of Adjacent Elements With the Same Color
// https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/


func colorTheArray(n int, queries [][]int) []int {
	colors := make([]int, n)
	ans := make([]int, len(queries))
	same := 0
	for i, q := range queries {
		idx, color := q[0], q[1]
		if colors[idx] != 0 {
			if idx > 0 && colors[idx] == colors[idx-1] {
				same--
			}
			if idx+1 < n && colors[idx] == colors[idx+1] {
				same--
			}
		}
		colors[idx] = color
		if idx > 0 && colors[idx] == colors[idx-1] {
			same++
		}
		if idx+1 < n && colors[idx] == colors[idx+1] {
			same++
		}
		ans[i] = same
	}
	return ans
}
