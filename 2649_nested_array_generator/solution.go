// LeetCode 2649 - Nested Array Generator
// https://leetcode.com/problems/nested-array-generator/


func inorderTraversal(arr []interface{}) []int {
	out := []int{}
	var dfs func(interface{})
	dfs = func(x interface{}) {
		switch v := x.(type) {
		case int:
			out = append(out, v)
		case float64:
			out = append(out, int(v))
		case []interface{}:
			for _, e := range v {
				dfs(e)
			}
		}
	}
	for _, e := range arr {
		dfs(e)
	}
	return out
}
