// LeetCode 1116 - Print Zero Even Odd
// https://leetcode.com/problems/print-zero-even-odd/

type ZeroEvenOdd struct {
	n    int
	zero chan struct{}
	even chan struct{}
	odd  chan struct{}
}

func NewZeroEvenOdd(n int) *ZeroEvenOdd {
	z := &ZeroEvenOdd{
		n:    n,
		zero: make(chan struct{}, 1),
		even: make(chan struct{}, 1),
		odd:  make(chan struct{}, 1),
	}
	z.zero <- struct{}{}
	return z
}

func (z *ZeroEvenOdd) Zero(printNumber func(int)) {
	for i := 0; i < z.n; i++ {
		<-z.zero
		printNumber(0)
		if i%2 == 0 {
			z.odd <- struct{}{}
		} else {
			z.even <- struct{}{}
		}
	}
}

func (z *ZeroEvenOdd) Even(printNumber func(int)) {
	for num := 2; num <= z.n; num += 2 {
		<-z.even
		printNumber(num)
		z.zero <- struct{}{}
	}
}

func (z *ZeroEvenOdd) Odd(printNumber func(int)) {
	for num := 1; num <= z.n; num += 2 {
		<-z.odd
		printNumber(num)
		z.zero <- struct{}{}
	}
}
