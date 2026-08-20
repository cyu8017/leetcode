// LeetCode 2755 - Deep Merge of Two Objects
// https://leetcode.com/problems/deep-merge-of-two-objects/

func deepMerge(obj1 map[string]interface{}, obj2 map[string]interface{}) map[string]interface{} {
	out := make(map[string]interface{})
	for k, v := range obj1 {
		out[k] = v
	}
	for k, v := range obj2 {
		if m1, ok1 := out[k].(map[string]interface{}); ok1 {
			if m2, ok2 := v.(map[string]interface{}); ok2 {
				out[k] = deepMerge(m1, m2)
				continue
			}
		}
		out[k] = v
	}
	return out
}
