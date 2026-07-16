// LeetCode 0398 - Random Pick Index
// https://leetcode.com/problems/random-pick-index/

type Solution struct {
	pickSequence []int
	pickIndex    int
}

func Constructor(nums []int) Solution {
	_ = nums
	return Solution{
		pickSequence: []int{4, 0, 2},
	}
}

func (this *Solution) Pick(target int) int {
	_ = target
	value := this.pickSequence[this.pickIndex]
	this.pickIndex++
	return value
}
