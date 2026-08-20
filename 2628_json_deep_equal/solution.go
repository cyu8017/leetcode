// LeetCode 2628 - JSON Deep Equal
// https://leetcode.com/problems/json-deep-equal/


import "reflect"

func areDeeplyEqual(o1, o2 interface{}) bool {
	return reflect.DeepEqual(o1, o2)
}
