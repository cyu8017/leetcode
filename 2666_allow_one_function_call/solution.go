// LeetCode 2666 - Allow One Function Call
// https://leetcode.com/problems/allow-one-function-call/


func once(fn func(...interface{}) interface{}) func(...interface{}) interface{} {
	called := false
	var res interface{}
	return func(args ...interface{}) interface{} {
		if called {
			return nil
		}
		called = true
		res = fn(args...)
		return res
	}
}
