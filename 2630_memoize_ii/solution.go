// LeetCode 2630 - Memoize II
// https://leetcode.com/problems/memoize-ii/


func memoizeII(fn func(...interface{}) interface{}) func(...interface{}) interface{} {
	type key struct{ s string }
	cache := map[string]interface{}{}
	return func(args ...interface{}) interface{} {
		k := ""
		for _, a := range args {
			k += "|" + toStr2630(a)
		}
		if v, ok := cache[k]; ok {
			return v
		}
		v := fn(args...)
		cache[k] = v
		return v
	}
}
func toStr2630(a interface{}) string {
	return ""
}
