// LeetCode 1671 - Minimum Number of Removals to Make Mountain Array
// https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/

import "sort"

func minimumMountainRemovals(nums []int) int {
	lis := func(a []int) []int {
		d := []int{}
		out := make([]int, len(a))
		for i, x := range a {
			j := sort.SearchInts(d, x)
			if j == len(d) {
				d = append(d, x)
			} else {
				d[j] = x
			}
			out[i] = j + 1
		}
		return out
	}
	n := len(nums)
	l := lis(nums)
	rev := make([]int, n)
	for i := 0; i < n; i++ {
		rev[i] = nums[n-1-i]
	}
	rRev := lis(rev)
	r := make([]int, n)
	for i := 0; i < n; i++ {
		r[i] = rRev[n-1-i]
	}
	best := 0
	for i := 0; i < n; i++ {
		if l[i] > 1 && r[i] > 1 {
			if l[i]+r[i]-1 > best {
				best = l[i] + r[i] - 1
			}
		}
	}
	return n - best
}
