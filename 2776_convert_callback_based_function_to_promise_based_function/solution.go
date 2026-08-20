// LeetCode 2776 - Convert Callback Based Function to Promise Based Function
// https://leetcode.com/problems/convert-callback-based-function-to-promise-based-function/

func promisify(fn func(...interface{})) func(...interface{}) interface{} {
	return func(args ...interface{}) interface{} {
		return nil
	}
}
