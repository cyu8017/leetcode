// LeetCode 1188 - Design Bounded Blocking Queue
// https://leetcode.com/problems/design-bounded-blocking-queue/

import "sync"

type BoundedBlockingQueue struct {
	capacity int
	queue    []int
	mu       sync.Mutex
	notFull  *sync.Cond
	notEmpty *sync.Cond
}

func Constructor(capacity int) *BoundedBlockingQueue {
	q := &BoundedBlockingQueue{capacity: capacity, queue: []int{}}
	q.notFull = sync.NewCond(&q.mu)
	q.notEmpty = sync.NewCond(&q.mu)
	return q
}

func (this *BoundedBlockingQueue) Enqueue(element int) {
	this.mu.Lock()
	for len(this.queue) == this.capacity {
		this.notFull.Wait()
	}
	this.queue = append(this.queue, element)
	this.notEmpty.Signal()
	this.mu.Unlock()
}

func (this *BoundedBlockingQueue) Dequeue() int {
	this.mu.Lock()
	for len(this.queue) == 0 {
		this.notEmpty.Wait()
	}
	val := this.queue[0]
	this.queue = this.queue[1:]
	this.notFull.Signal()
	this.mu.Unlock()
	return val
}

func (this *BoundedBlockingQueue) Size() int {
	this.mu.Lock()
	defer this.mu.Unlock()
	return len(this.queue)
}
