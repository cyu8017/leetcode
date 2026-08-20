// LeetCode 0641 - Design Circular Deque
// https://leetcode.com/problems/design-circular-deque/

type MyCircularDeque struct {
	data     []int
	capacity int
	front    int
	size     int
}

func Constructor(k int) MyCircularDeque {
	return MyCircularDeque{data: make([]int, k), capacity: k}
}

func (q *MyCircularDeque) InsertFront(value int) bool {
	if q.IsFull() {
		return false
	}
	q.front = (q.front - 1 + q.capacity) % q.capacity
	q.data[q.front] = value
	q.size++
	return true
}

func (q *MyCircularDeque) InsertLast(value int) bool {
	if q.IsFull() {
		return false
	}
	q.data[(q.front+q.size)%q.capacity] = value
	q.size++
	return true
}

func (q *MyCircularDeque) DeleteFront() bool {
	if q.IsEmpty() {
		return false
	}
	q.front = (q.front + 1) % q.capacity
	q.size--
	return true
}

func (q *MyCircularDeque) DeleteLast() bool {
	if q.IsEmpty() {
		return false
	}
	q.size--
	return true
}

func (q *MyCircularDeque) GetFront() int {
	if q.IsEmpty() {
		return -1
	}
	return q.data[q.front]
}

func (q *MyCircularDeque) GetRear() int {
	if q.IsEmpty() {
		return -1
	}
	return q.data[(q.front+q.size-1)%q.capacity]
}

func (q *MyCircularDeque) IsEmpty() bool {
	return q.size == 0
}

func (q *MyCircularDeque) IsFull() bool {
	return q.size == q.capacity
}
