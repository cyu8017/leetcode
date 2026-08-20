// LeetCode 2759 - Convert JSON String to Object
// https://leetcode.com/problems/convert-json-string-to-object/

import "encoding/json"

func jsonParse(str string) interface{} {
	var v interface{}
	_ = json.Unmarshal([]byte(str), &v)
	return v
}
