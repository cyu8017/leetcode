// LeetCode 2794 - Create Object from Two Arrays
// https://leetcode.com/problems/create-object-from-two-arrays/

func createObject(keysArr []string, valuesArr []interface{}) map[string]interface{} {
	out := map[string]interface{}{}
	n := len(keysArr)
	if len(valuesArr) < n {
		n = len(valuesArr)
	}
	for i := 0; i < n; i++ {
		if _, ok := out[keysArr[i]]; !ok {
			out[keysArr[i]] = valuesArr[i]
		}
	}
	return out
}
