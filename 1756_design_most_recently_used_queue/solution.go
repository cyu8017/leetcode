// LeetCode 1756 - Design Most Recently Used Queue
// https://leetcode.com/problems/design-most-recently-used-queue/

type MRUQueue struct {
	q []int
}

func Constructor(n int) MRUQueue {
	q := make([]int, n)
	for i := 0; i < n; i++ {
		q[i] = i + 1
	}
	return MRUQueue{q: q}
}

func (this *MRUQueue) Fetch(k int) int {
	val := this.q[k-1]
	this.q = append(this.q[:k-1], this.q[k:]...)
	this.q = append(this.q, val)
	return val
}
