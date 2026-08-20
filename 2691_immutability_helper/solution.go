// LeetCode 2691 - Immutability Helper
// https://leetcode.com/problems/immutability-helper/


func immutableHelper(obj map[string]interface{}, mutators []func(map[string]interface{})) []map[string]interface{} {
	out := []map[string]interface{}{}
	cur := clone2691(obj)
	out = append(out, clone2691(cur))
	for _, m := range mutators {
		next := clone2691(cur)
		m(next)
		cur = next
		out = append(out, clone2691(cur))
	}
	return out
}
func clone2691(m map[string]interface{}) map[string]interface{} {
	n := map[string]interface{}{}
	for k, v := range m {
		n[k] = v
	}
	return n
}
