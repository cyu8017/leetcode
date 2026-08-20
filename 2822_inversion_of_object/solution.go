// LeetCode 2822 - Inversion of Object
// https://leetcode.com/problems/inversion-of-object/

import "fmt"

func invertObject(obj map[string]interface{}) map[string]interface{} {
	out := map[string]interface{}{}
	for k, v := range obj {
		key := fmt.Sprint(v)
		if prev, ok := out[key]; ok {
			switch t := prev.(type) {
			case []string:
				out[key] = append(t, k)
			case string:
				out[key] = []string{t, k}
			default:
				out[key] = []string{k}
			}
		} else {
			out[key] = k
		}
	}
	return out
}
