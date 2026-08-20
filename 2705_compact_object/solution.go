// LeetCode 2705 - Compact Object
// https://leetcode.com/problems/compact-object/


func compactObject(obj interface{}) interface{} {
	switch v := obj.(type) {
	case []interface{}:
		out := []interface{}{}
		for _, e := range v {
			c := compactObject(e)
			if isTruthy2705(c) {
				out = append(out, c)
			}
		}
		return out
	case map[string]interface{}:
		out := map[string]interface{}{}
		for k, e := range v {
			c := compactObject(e)
			if isTruthy2705(c) {
				out[k] = c
			}
		}
		return out
	default:
		return obj
	}
}
func isTruthy2705(v interface{}) bool {
	if v == nil {
		return false
	}
	if b, ok := v.(bool); ok {
		return b
	}
	return true
}
