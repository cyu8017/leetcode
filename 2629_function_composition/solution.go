// LeetCode 2629 - Function Composition
// https://leetcode.com/problems/function-composition/


func compose(functions []func(int) int) func(int) int {
	return func(x int) int {
		for i := len(functions) - 1; i >= 0; i-- {
			x = functions[i](x)
		}
		return x
	}
}
