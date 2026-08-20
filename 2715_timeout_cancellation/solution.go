// LeetCode 2715 - Timeout Cancellation
// https://leetcode.com/problems/timeout-cancellation/


import "time"

func cancellable(fn func(...interface{}) interface{}, args []interface{}, t int) (func(), <-chan interface{}) {
	cancelled := false
	ch := make(chan interface{}, 1)
	timer := time.AfterFunc(time.Duration(t)*time.Millisecond, func() {
		if !cancelled {
			ch <- fn(args...)
		}
		close(ch)
	})
	cancel := func() {
		cancelled = true
		timer.Stop()
	}
	return cancel, ch
}
