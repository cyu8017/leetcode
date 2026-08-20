// LeetCode 3695 - Maximize Alternating Sum Using Swaps
// https://leetcode.com/problems/maximize-alternating-sum-using-swaps/

import (
	"sort"
)

func maxAlternatingSum(nums []int, swaps [][]int) int64 {
	n := len(nums)
	parent := make([]int, n)
	for i := range parent {
		parent[i] = i
	}
	var find func(int) int
	find = func(x int) int {
		if parent[x] != x {
			parent[x] = find(parent[x])
		}
		return parent[x]
	}
	for _, s := range swaps {
		a, b := find(s[0]), find(s[1])
		if a != b {
			parent[a] = b
		}
	}
	compVals := map[int][]int{}
	compIdx := map[int][]int{}
	for i := 0; i < n; i++ {
		r := find(i)
		compVals[r] = append(compVals[r], nums[i])
		compIdx[r] = append(compIdx[r], i)
	}
	arr := make([]int, n)
	for r, vals := range compVals {
		idxs := compIdx[r]
		sort.Ints(vals)
		sort.Sort(sort.Reverse(sort.IntSlice(vals)))
		// assign largest to even indices preferentially within component
		even, odd := []int{}, []int{}
		for _, i := range idxs {
			if i%2 == 0 {
				even = append(even, i)
			} else {
				odd = append(odd, i)
			}
		}
		sort.Ints(even)
		sort.Ints(odd)
		// take largest |even| values for even positions
		ei := 0
		for _, v := range vals {
			if ei < len(even) {
				arr[even[ei]] = v
				ei++
			} else {
				arr[odd[ei-len(even)]] = v
				ei++
			}
		}
		_ = r
	}
	var ans int64
	for i, v := range arr {
		if i%2 == 0 {
			ans += int64(v)
		} else {
			ans -= int64(v)
		}
	}
	return ans
}
