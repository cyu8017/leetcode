// LeetCode 2823 - Deep Object Filter
// https://leetcode.com/problems/deep-object-filter/

func deepFilter(obj interface{}, fn func(interface{}) bool) interface{} {
	switch t := obj.(type) {
	case []interface{}:
		out := []interface{}{}
		for _, v := range t {
			fv := deepFilter(v, fn)
			if fv != nil {
				out = append(out, fv)
			}
		}
		if len(out) == 0 {
			return nil
		}
		return out
	case map[string]interface{}:
		out := map[string]interface{}{}
		for k, v := range t {
			fv := deepFilter(v, fn)
			if fv != nil {
				out[k] = fv
			}
		}
		if len(out) == 0 {
			return nil
		}
		return out
	default:
		if fn(obj) {
			return obj
		}
		return nil
	}
}
