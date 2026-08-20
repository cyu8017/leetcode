// LeetCode 2675 - Array of Objects to Matrix
// https://leetcode.com/problems/array-of-objects-to-matrix/


import "sort"

func jsonToMatrix(arr []map[string]interface{}) [][]string {
	keys := map[string]bool{}
	for _, obj := range arr {
		for k := range obj {
			keys[k] = true
		}
	}
	cols := []string{}
	for k := range keys {
		cols = append(cols, k)
	}
	sort.Strings(cols)
	mat := [][]string{cols}
	for _, obj := range arr {
		row := make([]string, len(cols))
		for i, k := range cols {
			if v, ok := obj[k]; ok {
				row[i] = toStr2675(v)
			} else {
				row[i] = ""
			}
		}
		mat = append(mat, row)
	}
	return mat
}
func toStr2675(v interface{}) string {
	switch x := v.(type) {
	case string:
		return x
	default:
		return ""
	}
}
