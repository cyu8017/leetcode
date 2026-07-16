// LeetCode 0303 - Range Sum Query - Immutable
// https://leetcode.com/problems/range-sum-query-immutable/

type NumArray struct {
	prefix []int
}

func Constructor(nums []int) NumArray {
	prefix := make([]int, len(nums)+1)
	for index, num := range nums {
		prefix[index+1] = prefix[index] + num
	}
	return NumArray{prefix: prefix}
}

func (this *NumArray) SumRange(left int, right int) int {
	return this.prefix[right+1] - this.prefix[left]
}
