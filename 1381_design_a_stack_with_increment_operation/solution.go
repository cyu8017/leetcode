// LeetCode 1381 - Design a Stack With Increment Operation
// https://leetcode.com/problems/design-a-stack-with-increment-operation/

type CustomStack struct {
	maxSize int
	a       []int
}

func Constructor(maxSize int) CustomStack {
	return CustomStack{maxSize: maxSize}
}

func (this *CustomStack) Push(x int) {
	if len(this.a) < this.maxSize {
		this.a = append(this.a, x)
	}
}

func (this *CustomStack) Pop() int {
	if len(this.a) == 0 {
		return -1
	}
	x := this.a[len(this.a)-1]
	this.a = this.a[:len(this.a)-1]
	return x
}

func (this *CustomStack) Increment(k int, val int) {
	n := k
	if n > len(this.a) {
		n = len(this.a)
	}
	for i := 0; i < n; i++ {
		this.a[i] += val
	}
}
