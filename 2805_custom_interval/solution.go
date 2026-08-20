// LeetCode 2805 - Custom Interval
// https://leetcode.com/problems/custom-interval/

import "time"

func customInterval(fn func(), delay, period int) func() {
	cancelled := false
	go func() {
		time.Sleep(time.Duration(delay) * time.Millisecond)
		for !cancelled {
			fn()
			time.Sleep(time.Duration(period) * time.Millisecond)
		}
	}()
	return func() { cancelled = true }
}
