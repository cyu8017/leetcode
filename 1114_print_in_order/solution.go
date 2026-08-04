// LeetCode 1114 - Print in Order
// https://leetcode.com/problems/print-in-order/

type Foo struct {
	second chan struct{}
	third  chan struct{}
}

func Constructor() *Foo {
	return &Foo{
		second: make(chan struct{}),
		third:  make(chan struct{}),
	}
}

func (f *Foo) First(printFirst func()) {
	printFirst()
	close(f.second)
}

func (f *Foo) Second(printSecond func()) {
	<-f.second
	printSecond()
	close(f.third)
}

func (f *Foo) Third(printThird func()) {
	<-f.third
	printThird()
}
