// LeetCode 2627 - Debounce
// https://leetcode.com/problems/debounce/


import "sync"
import "time"

func debounce(fn func(...interface{}), t int) func(...interface{}) {
	var mu sync.Mutex
	var timer *time.Timer
	return func(args ...interface{}) {
		mu.Lock()
		defer mu.Unlock()
		if timer != nil {
			timer.Stop()
		}
		timer = time.AfterFunc(time.Duration(t)*time.Millisecond, func() {
			fn(args...)
		})
	}
}
