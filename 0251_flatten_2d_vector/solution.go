// LeetCode 0251 - Flatten 2D Vector
// https://leetcode.com/problems/flatten-2d-vector/

type Vector2D struct {
	vec  [][]int
	row  int
	col  int
}

func Constructor(vec [][]int) Vector2D {
	iterator := Vector2D{vec: vec}
	iterator.advance()
	return iterator
}

func (this *Vector2D) advance() {
	for this.row < len(this.vec) && this.col >= len(this.vec[this.row]) {
		this.row++
		this.col = 0
	}
}

func (this *Vector2D) Next() int {
	value := this.vec[this.row][this.col]
	this.col++
	this.advance()
	return value
}

func (this *Vector2D) HasNext() bool {
	this.advance()
	return this.row < len(this.vec)
}
