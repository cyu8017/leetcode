// LeetCode 1195 - Fizz Buzz Multithreaded
// https://leetcode.com/problems/fizz-buzz-multithreaded/

import "sync"

type FizzBuzz struct {
	n       int
	current int
	cond    *sync.Cond
}

func NewFizzBuzz(n int) *FizzBuzz {
	fb := &FizzBuzz{n: n, current: 1}
	fb.cond = sync.NewCond(&sync.Mutex{})
	return fb
}

func (fb *FizzBuzz) run(pred func(int) bool, action func()) {
	fb.cond.L.Lock()
	defer fb.cond.L.Unlock()
	for fb.current <= fb.n {
		if pred(fb.current) {
			action()
			fb.current++
			fb.cond.Broadcast()
		} else {
			fb.cond.Wait()
		}
	}
}

func (fb *FizzBuzz) Fizz(printFizz func()) {
	fb.run(func(x int) bool { return x%3 == 0 && x%5 != 0 }, printFizz)
}

func (fb *FizzBuzz) Buzz(printBuzz func()) {
	fb.run(func(x int) bool { return x%5 == 0 && x%3 != 0 }, printBuzz)
}

func (fb *FizzBuzz) Fizzbuzz(printFizzBuzz func()) {
	fb.run(func(x int) bool { return x%15 == 0 }, printFizzBuzz)
}

func (fb *FizzBuzz) Number(printNumber func(int)) {
	fb.run(func(x int) bool { return x%3 != 0 && x%5 != 0 }, func() { printNumber(fb.current) })
}
