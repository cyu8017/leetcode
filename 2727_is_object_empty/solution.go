// LeetCode 2727 - Is Object Empty
// https://leetcode.com/problems/is-object-empty/


func isEmpty(obj interface{}) bool {
	switch v := obj.(type) {
	case map[string]interface{}:
		return len(v) == 0
	case []interface{}:
		return len(v) == 0
	default:
		return true
	}
}
