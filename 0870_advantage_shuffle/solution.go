// LeetCode 0870 - Advantage Shuffle
// https://leetcode.com/problems/advantage-shuffle/

import "sort"

func advantageCount(nums1 []int, nums2 []int) []int {
	sorted1 := append([]int{}, nums1...)
	sort.Ints(sorted1)
	type pair struct{ i, val int }
	order := make([]pair, len(nums2))
	for i, v := range nums2 {
		order[i] = pair{i, v}
	}
	sort.Slice(order, func(i, j int) bool { return order[i].val > order[j].val })
	ans := make([]int, len(nums1))
	lo, hi := 0, len(sorted1)-1
	for _, p := range order {
		if sorted1[hi] > p.val {
			ans[p.i] = sorted1[hi]
			hi--
		} else {
			ans[p.i] = sorted1[lo]
			lo++
		}
	}
	return ans
}
