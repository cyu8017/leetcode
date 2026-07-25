// LeetCode 1670 - Design Front Middle Back Queue
// https://leetcode.com/problems/design-front-middle-back-queue/

type FrontMiddleBackQueue struct {
	l, r []int
}

func Constructor() FrontMiddleBackQueue {
	return FrontMiddleBackQueue{}
}

func (this *FrontMiddleBackQueue) bal() {
	for len(this.l) > len(this.r)+1 {
		this.r = append([]int{this.l[len(this.l)-1]}, this.r...)
		this.l = this.l[:len(this.l)-1]
	}
	for len(this.r) > len(this.l) {
		this.l = append(this.l, this.r[0])
		this.r = this.r[1:]
	}
}

func (this *FrontMiddleBackQueue) PushFront(val int) {
	this.l = append([]int{val}, this.l...)
	this.bal()
}

func (this *FrontMiddleBackQueue) PushMiddle(val int) {
	if len(this.l) > len(this.r) {
		this.r = append([]int{this.l[len(this.l)-1]}, this.r...)
		this.l = this.l[:len(this.l)-1]
	}
	this.l = append(this.l, val)
}

func (this *FrontMiddleBackQueue) PushBack(val int) {
	this.r = append(this.r, val)
	this.bal()
}

func (this *FrontMiddleBackQueue) PopFront() int {
	if len(this.l) == 0 {
		return -1
	}
	v := this.l[0]
	this.l = this.l[1:]
	this.bal()
	return v
}

func (this *FrontMiddleBackQueue) PopMiddle() int {
	if len(this.l) == 0 {
		return -1
	}
	v := this.l[len(this.l)-1]
	this.l = this.l[:len(this.l)-1]
	this.bal()
	return v
}

func (this *FrontMiddleBackQueue) PopBack() int {
	if len(this.l) == 0 {
		return -1
	}
	var v int
	if len(this.r) > 0 {
		v = this.r[len(this.r)-1]
		this.r = this.r[:len(this.r)-1]
	} else {
		v = this.l[len(this.l)-1]
		this.l = this.l[:len(this.l)-1]
	}
	this.bal()
	return v
}
