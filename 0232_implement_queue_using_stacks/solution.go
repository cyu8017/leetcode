// LeetCode 0232 - Implement Queue using Stacks
// https://leetcode.com/problems/implement-queue-using-stacks/

type MyQueue struct {
	inputStack  []int
	outputStack []int
}

func Constructor() MyQueue {
	return MyQueue{}
}

func (this *MyQueue) move() {
	if len(this.outputStack) == 0 {
		for len(this.inputStack) > 0 {
			top := this.inputStack[len(this.inputStack)-1]
			this.inputStack = this.inputStack[:len(this.inputStack)-1]
			this.outputStack = append(this.outputStack, top)
		}
	}
}

func (this *MyQueue) Push(x int) {
	this.inputStack = append(this.inputStack, x)
}

func (this *MyQueue) Pop() int {
	this.move()
	top := this.outputStack[len(this.outputStack)-1]
	this.outputStack = this.outputStack[:len(this.outputStack)-1]
	return top
}

func (this *MyQueue) Peek() int {
	this.move()
	return this.outputStack[len(this.outputStack)-1]
}

func (this *MyQueue) Empty() bool {
	return len(this.inputStack) == 0 && len(this.outputStack) == 0
}
