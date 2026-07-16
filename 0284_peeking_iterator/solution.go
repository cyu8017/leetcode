// LeetCode 0284 - Peeking Iterator
// https://leetcode.com/problems/peeking-iterator/

type Iterator struct {
	nums []int
	idx  int
}

func (this *Iterator) Next() int {
	value := this.nums[this.idx]
	this.idx++
	return value
}

func (this *Iterator) HasNext() bool {
	return this.idx < len(this.nums)
}

type PeekingIterator struct {
	iterator   *Iterator
	peeked     int
	hasPeeked  bool
}

func Constructor(iter *Iterator) *PeekingIterator {
	return &PeekingIterator{iterator: iter}
}

func (this *PeekingIterator) Peek() int {
	if !this.hasPeeked {
		this.peeked = this.iterator.Next()
		this.hasPeeked = true
	}
	return this.peeked
}

func (this *PeekingIterator) Next() int {
	if this.hasPeeked {
		this.hasPeeked = false
		return this.peeked
	}
	return this.iterator.Next()
}

func (this *PeekingIterator) HasNext() bool {
	return this.hasPeeked || this.iterator.HasNext()
}
