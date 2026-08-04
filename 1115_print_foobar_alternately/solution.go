// LeetCode 1115 - Print FooBar Alternately
// https://leetcode.com/problems/print-foobar-alternately/

type FooBar struct {
	n    int
	fooS chan struct{}
	barS chan struct{}
}

func NewFooBar(n int) *FooBar {
	fb := &FooBar{
		n:    n,
		fooS: make(chan struct{}, 1),
		barS: make(chan struct{}, 1),
	}
	fb.fooS <- struct{}{}
	return fb
}

func (fb *FooBar) Foo(printFoo func()) {
	for i := 0; i < fb.n; i++ {
		<-fb.fooS
		printFoo()
		fb.barS <- struct{}{}
	}
}

func (fb *FooBar) Bar(printBar func()) {
	for i := 0; i < fb.n; i++ {
		<-fb.barS
		printBar()
		fb.fooS <- struct{}{}
	}
}
