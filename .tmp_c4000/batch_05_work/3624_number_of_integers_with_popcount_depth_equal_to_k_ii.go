// LeetCode 3624 - Number of Integers With Popcount Depth Equal to K II
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-ii/

import "math/bits"

func popcountDepth(nums []int64, queries [][]int64) []int {
	depth := func(x int64) int {
		if x == 1 {
			return 0
		}
		d := 0
		for x > 1 {
			x = int64(bits.OnesCount64(uint64(x)))
			d++
		}
		return d
	}
	a := append([]int64(nil), nums...)
	var ans []int
	for _, q := range queries {
		if q[0] == 1 {
			l, r, k := int(q[1]), int(q[2]), int(q[3])
			cnt := 0
			for i := l; i <= r; i++ {
				if depth(a[i]) == k {
					cnt++
				}
			}
			ans = append(ans, cnt)
		} else {
			idx := int(q[1])
			a[idx] = q[2]
		}
	}
	return ans
}
