// LeetCode 0622 - Design Circular Queue
// https://leetcode.com/problems/design-circular-queue/

type MyCircularQueue struct {
	data     []int
	capacity int
	head     int
	size     int
}

func Constructor(k int) MyCircularQueue {
	return MyCircularQueue{data: make([]int, k), capacity: k}
}

func (q *MyCircularQueue) EnQueue(value int) bool {
	if q.IsFull() {
		return false
	}
	q.data[(q.head+q.size)%q.capacity] = value
	q.size++
	return true
}

func (q *MyCircularQueue) DeQueue() bool {
	if q.IsEmpty() {
		return false
	}
	q.head = (q.head + 1) % q.capacity
	q.size--
	return true
}

func (q *MyCircularQueue) Front() int {
	if q.IsEmpty() {
		return -1
	}
	return q.data[q.head]
}

func (q *MyCircularQueue) Rear() int {
	if q.IsEmpty() {
		return -1
	}
	return q.data[(q.head+q.size-1)%q.capacity]
}

func (q *MyCircularQueue) IsEmpty() bool {
	return q.size == 0
}

func (q *MyCircularQueue) IsFull() bool {
	return q.size == q.capacity
}
