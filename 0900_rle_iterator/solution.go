// LeetCode 0900 - RLE Iterator
// https://leetcode.com/problems/rle-iterator/

type RLEIterator struct {
	enc []int
	i   int
}

func Constructor(encoding []int) RLEIterator {
	return RLEIterator{enc: encoding}
}

func (this *RLEIterator) Next(n int) int {
	for this.i < len(this.enc) {
		if this.enc[this.i] >= n {
			this.enc[this.i] -= n
			return this.enc[this.i+1]
		}
		n -= this.enc[this.i]
		this.i += 2
	}
	return -1
}
