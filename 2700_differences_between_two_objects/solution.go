// LeetCode 2700 - Differences Between Two Objects
// https://leetcode.com/problems/differences-between-two-objects/


func objDiff(obj1, obj2 map[string]interface{}) map[string]interface{} {
	out := map[string]interface{}{}
	for k, v1 := range obj1 {
		v2, ok := obj2[k]
		if !ok {
			continue
		}
		m1, ok1 := v1.(map[string]interface{})
		m2, ok2 := v2.(map[string]interface{})
		if ok1 && ok2 {
			sub := objDiff(m1, m2)
			if len(sub) > 0 {
				out[k] = sub
			}
		} else if v1 != v2 {
			out[k] = []interface{}{v1, v2}
		}
	}
	return out
}
