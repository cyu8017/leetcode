// LeetCode 0716 - Max Stack
// https://leetcode.com/problems/max-stack/

type MaxStack struct {
	stack []int
	maxes []int
}

func Constructor() MaxStack {
	return MaxStack{}
}

func (this *MaxStack) Push(x int) {
	this.stack = append(this.stack, x)
	if len(this.maxes) == 0 || x > this.maxes[len(this.maxes)-1] {
		this.maxes = append(this.maxes, x)
	} else {
		this.maxes = append(this.maxes, this.maxes[len(this.maxes)-1])
	}
}

func (this *MaxStack) Pop() int {
	this.maxes = this.maxes[:len(this.maxes)-1]
	x := this.stack[len(this.stack)-1]
	this.stack = this.stack[:len(this.stack)-1]
	return x
}

func (this *MaxStack) Top() int {
	return this.stack[len(this.stack)-1]
}

func (this *MaxStack) PeekMax() int {
	return this.maxes[len(this.maxes)-1]
}

func (this *MaxStack) PopMax() int {
	maxVal := this.PeekMax()
	buffer := []int{}
	for this.Top() != maxVal {
		buffer = append(buffer, this.Pop())
	}
	this.Pop()
	for i := len(buffer) - 1; i >= 0; i-- {
		this.Push(buffer[i])
	}
	return maxVal
}
