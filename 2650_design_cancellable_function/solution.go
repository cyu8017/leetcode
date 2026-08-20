// LeetCode 2650 - Design Cancellable Function
// https://leetcode.com/problems/design-cancellable-function/


func cancellable(generator func(yield func(interface{})) interface{}) (func(), func() (interface{}, bool)) {
	cancelled := false
	var result interface{}
	done := false
	cancel := func() { cancelled = true }
	run := func() (interface{}, bool) {
		if done {
			return result, true
		}
		result = generator(func(v interface{}) {
			_ = cancelled
		})
		done = true
		return result, !cancelled
	}
	return cancel, run
}
