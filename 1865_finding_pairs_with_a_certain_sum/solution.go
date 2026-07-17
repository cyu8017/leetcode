// LeetCode 1865 - Finding Pairs With a Certain Sum
// https://leetcode.com/problems/finding-pairs-with-a-certain-sum/

type FindSumPairs struct {
	nums1  []int
	nums2  []int
	counts map[int]int
}

func Constructor(nums1 []int, nums2 []int) FindSumPairs {
	counts := make(map[int]int)
	for _, num := range nums2 {
		counts[num]++
	}
	return FindSumPairs{nums1: nums1, nums2: nums2, counts: counts}
}

func (this *FindSumPairs) Add(index int, val int) {
	this.counts[this.nums2[index]]--
	this.nums2[index] += val
	this.counts[this.nums2[index]]++
}

func (this *FindSumPairs) Count(tot int) int {
	result := 0
	for _, num := range this.nums1 {
		result += this.counts[tot-num]
	}
	return result
}
