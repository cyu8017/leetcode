// LeetCode 1157 - Online Majority Element In Subarray
// https://leetcode.com/problems/online-majority-element-in-subarray/

import "sort"

type MajorityChecker struct {
	arr []int
	pos map[int][]int
}

func Constructor(arr []int) MajorityChecker {
	pos := map[int][]int{}
	for i, v := range arr {
		pos[v] = append(pos[v], i)
	}
	return MajorityChecker{arr: arr, pos: pos}
}

func (this *MajorityChecker) Query(left int, right int, threshold int) int {
	span := right - left + 1
	seen := map[int]bool{}
	for t := 0; t < 30 && t < span; t++ {
		cand := this.arr[left+(t*7919+13)%span]
		if seen[cand] {
			continue
		}
		seen[cand] = true
		arr := this.pos[cand]
		lo := sort.SearchInts(arr, left)
		hi := sort.Search(len(arr), func(i int) bool { return arr[i] > right })
		if hi-lo >= threshold {
			return cand
		}
	}
	return -1
}
