// LeetCode 2633 - Convert Object to JSON String
// https://leetcode.com/problems/convert-object-to-json-string/


import "encoding/json"

func jsonStringify(object interface{}) string {
	b, _ := json.Marshal(object)
	return string(b)
}
