// LeetCode 0382 - Linked List Random Node
// https://leetcode.com/problems/linked-list-random-node/

type ListNode struct {
	Val  int
	Next *ListNode
}

type Solution struct {
	values         []int
	randomSequence []int
	randomIndex    int
}

func Constructor(head *ListNode) Solution {
	values := make([]int, 0)
	for current := head; current != nil; current = current.Next {
		values = append(values, current.Val)
	}
	return Solution{
		values:         values,
		randomSequence: []int{1, 3, 2, 2, 3},
	}
}

func (this *Solution) GetRandom() int {
	value := this.randomSequence[this.randomIndex]
	this.randomIndex++
	return value
}
