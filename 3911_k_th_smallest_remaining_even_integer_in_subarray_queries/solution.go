// LeetCode 3911 - K-th Smallest Remaining Even Integer in Subarray Queries
// https://leetcode.com/problems/k-th-smallest-remaining-even-integer-in-subarray-queries/

import "sort"

func kthSmallestEven(nums []int, queries [][]int) []int64 {
	evenPrefix := make([]int, len(nums)+1)
	for i, x := range nums {
		evenPrefix[i+1] = evenPrefix[i]
		if x%2 == 0 {
			evenPrefix[i+1]++
		}
	}
	ans := make([]int64, len(queries))
	for qi, q := range queries {
		l, r, k := q[0], q[1], int64(q[2])
		lo, hi := int64(1), k+int64(r-l+1)
		for lo < hi {
			mid := (lo + hi) / 2
			pos := sort.Search(len(nums), func(i int) bool {
				return int64(nums[i]) > 2*mid
			})
			if pos > r+1 {
				pos = r + 1
			}
			removed := 0
			if pos > l {
				removed = evenPrefix[pos] - evenPrefix[l]
			}
			if mid-int64(removed) >= k {
				hi = mid
			} else {
				lo = mid + 1
			}
		}
		ans[qi] = 2 * lo
	}
	return ans
}