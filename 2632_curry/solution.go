// LeetCode 2632 - Curry
// https://leetcode.com/problems/curry/


func curry(fn func(...int) int, arity int) interface{} {
	var next func([]int) interface{}
	next = func(args []int) interface{} {
		if len(args) >= arity {
			return fn(args[:arity]...)
		}
		return func(more ...int) interface{} {
			return next(append(append([]int{}, args...), more...))
		}
	}
	return next(nil)
}
