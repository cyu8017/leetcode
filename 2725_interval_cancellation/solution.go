// LeetCode 2725 - Interval Cancellation
// https://leetcode.com/problems/interval-cancellation/


import "time"

func cancellable(fn func(...interface{}), args []interface{}, t int) (func(), [][]interface{}) {
	times := [][]interface{}{}
	start := time.Now()
	fn(args...)
	times = append(times, []interface{}{fn(args...), 0})
	ticker := time.NewTicker(time.Duration(t) * time.Millisecond)
	stop := make(chan struct{})
	go func() {
		for {
			select {
			case <-ticker.C:
				elapsed := int(time.Since(start) / time.Millisecond)
				times = append(times, []interface{}{fn(args...), elapsed})
			case <-stop:
				ticker.Stop()
				return
			}
		}
	}()
	cancel := func() { close(stop) }
	return cancel, times
}
