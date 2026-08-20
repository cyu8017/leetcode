// LeetCode 2637 - Promise Time Limit
// https://leetcode.com/problems/promise-time-limit/


import "time"

func timeLimit(fn func() (interface{}, error), t int) func() (interface{}, error) {
	return func() (interface{}, error) {
		ch := make(chan struct {
			v interface{}
			e error
		}, 1)
		go func() {
			v, e := fn()
			ch <- struct {
				v interface{}
				e error
			}{v, e}
		}()
		select {
		case r := <-ch:
			return r.v, r.e
		case <-time.After(time.Duration(t) * time.Millisecond):
			return nil, errTimeLimit2637
		}
	}
}

var errTimeLimit2637 = &timeLimitError{}

type timeLimitError struct{}

func (e *timeLimitError) Error() string { return "Time Limit Exceeded" }
