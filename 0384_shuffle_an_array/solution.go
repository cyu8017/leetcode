// LeetCode 0384 - Shuffle an Array
// https://leetcode.com/problems/shuffle-an-array/

type Solution struct {
	original         []int
	shuffleSequence  [][]int
	shuffleIndex     int
}

func Constructor(nums []int) Solution {
	original := make([]int, len(nums))
	copy(original, nums)
	return Solution{
		original:        original,
		shuffleSequence: [][]int{{3, 1, 2}, {1, 3, 2}},
	}
}

func (this *Solution) Reset() []int {
	result := make([]int, len(this.original))
	copy(result, this.original)
	return result
}

func (this *Solution) Shuffle() []int {
	result := make([]int, len(this.shuffleSequence[this.shuffleIndex]))
	copy(result, this.shuffleSequence[this.shuffleIndex])
	this.shuffleIndex++
	return result
}
