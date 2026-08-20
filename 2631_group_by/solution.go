// LeetCode 2631 - Group By
// https://leetcode.com/problems/group-by/


func groupBy(arr []interface{}, fn func(interface{}) string) map[string][]interface{} {
	out := map[string][]interface{}{}
	for _, x := range arr {
		k := fn(x)
		out[k] = append(out[k], x)
	}
	return out
}
