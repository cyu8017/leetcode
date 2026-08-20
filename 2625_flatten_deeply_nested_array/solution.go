// LeetCode 2625 - Flatten Deeply Nested Array
// https://leetcode.com/problems/flatten-deeply-nested-array/


func flat(arr []interface{}, n int) []interface{} {
	var dfs func([]interface{}, int) []interface{}
	dfs = func(a []interface{}, depth int) []interface{} {
		out := []interface{}{}
		for _, x := range a {
			if sub, ok := x.([]interface{}); ok && depth < n {
				out = append(out, dfs(sub, depth+1)...)
			} else {
				out = append(out, x)
			}
		}
		return out
	}
	return dfs(arr, 0)
}
