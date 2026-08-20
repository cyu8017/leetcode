// LeetCode 2693 - Call Function with Custom Context
// https://leetcode.com/problems/call-function-with-custom-context/


func call(fn func(ctx interface{}, args ...interface{}) interface{}, ctx interface{}, args ...interface{}) interface{} {
	return fn(ctx, args...)
}
