// LeetCode 2665 - Counter II
// https://leetcode.com/problems/counter-ii/


type CounterII struct {
	init, cur int
}

func createCounter(init int) *CounterII {
	return &CounterII{init: init, cur: init}
}

func (c *CounterII) Increment() int {
	c.cur++
	return c.cur
}
func (c *CounterII) Decrement() int {
	c.cur--
	return c.cur
}
func (c *CounterII) Reset() int {
	c.cur = c.init
	return c.cur
}
