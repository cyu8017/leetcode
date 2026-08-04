// LeetCode 1570 - Dot Product of Two Sparse Vectors
// https://leetcode.com/problems/dot-product-of-two-sparse-vectors/

type SparseVector struct {
	values map[int]int
}

func Constructor(nums []int) SparseVector {
	values := map[int]int{}
	for i, x := range nums {
		if x != 0 {
			values[i] = x
		}
	}
	return SparseVector{values: values}
}

func (this *SparseVector) DotProduct(vec SparseVector) int {
	a, b := this.values, vec.values
	if len(a) > len(b) {
		a, b = b, a
	}
	ans := 0
	for i, x := range a {
		ans += x * b[i]
	}
	return ans
}

func dotProduct(nums1 []int, nums2 []int) int {
	v1 := Constructor(nums1)
	v2 := Constructor(nums2)
	return v1.DotProduct(v2)
}
