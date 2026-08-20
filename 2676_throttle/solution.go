// LeetCode 2676 - Throttle
// https://leetcode.com/problems/throttle/


import "sync"
import "time"

func throttle(fn func(...interface{}), t int) func(...interface{}) {
	var mu sync.Mutex
	var last int64
	return func(args ...interface{}) {
		mu.Lock()
		defer mu.Unlock()
		now := time.Now().UnixMilli()
		if now-last >= int64(t) {
			last = now
			fn(args...)
		}
	}
}
