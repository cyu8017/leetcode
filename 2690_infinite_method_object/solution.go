// LeetCode 2690 - Infinite Method Object
// https://leetcode.com/problems/infinite-method-object/


func createInfiniteObject() func(string) string {
	return func(name string) string {
		return name
	}
}
