// LeetCode 2821 - Delay the Resolution of Each Promise
// https://leetcode.com/problems/delay-the-resolution-of-each-promise/

import "time"

func delayAll(functions []func() interface{}, ms int) []func() interface{} {
	out := make([]func() interface{}, len(functions))
	for i, f := range functions {
		ff := f
		out[i] = func() interface{} {
			time.Sleep(time.Duration(ms) * time.Millisecond)
			return ff()
		}
	}
	return out
}
