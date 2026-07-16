// LeetCode 0281 - Zigzag Iterator
// https://leetcode.com/problems/zigzag-iterator/

type ZigzagIterator struct {
	vectors [][]int
	indices []int
	turn    int
}

func Constructor(v1, v2 []int) ZigzagIterator {
	return ZigzagIterator{
		vectors: [][]int{v1, v2},
		indices: []int{0, 0},
		turn:    0,
	}
}

func (this *ZigzagIterator) Next() int {
	for this.indices[this.turn] >= len(this.vectors[this.turn]) {
		this.turn = 1 - this.turn
	}
	value := this.vectors[this.turn][this.indices[this.turn]]
	this.indices[this.turn]++
	this.turn = 1 - this.turn
	return value
}

func (this *ZigzagIterator) HasNext() bool {
	for index := range this.vectors {
		if this.indices[index] < len(this.vectors[index]) {
			return true
		}
	}
	return false
}
