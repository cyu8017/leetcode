// LeetCode 0307 - Range Sum Query - Mutable
// https://leetcode.com/problems/range-sum-query-mutable/

type NumArray struct {
	nums  []int
	tree  []int
	size  int
}

func Constructor(nums []int) NumArray {
	obj := NumArray{
		nums: append([]int(nil), nums...),
		tree: make([]int, len(nums)+1),
		size: len(nums),
	}
	add := func(index, delta int) {
		for index <= obj.size {
			obj.tree[index] += delta
			index += index & -index
		}
	}
	for index, value := range nums {
		add(index+1, value)
	}
	return obj
}

func (this *NumArray) Update(index int, val int) {
	delta := val - this.nums[index]
	this.nums[index] = val
	for treeIndex := index + 1; treeIndex <= this.size; treeIndex += treeIndex & -treeIndex {
		this.tree[treeIndex] += delta
	}
}

func (this *NumArray) SumRange(left int, right int) int {
	prefix := func(index int) int {
		total := 0
		for index > 0 {
			total += this.tree[index]
			index -= index & -index
		}
		return total
	}
	return prefix(right+1) - prefix(left)
}
