// LeetCode 3422 - Minimum Operations to Make Subarray Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-subarray-elements-equal/

import "sort"

func minOperations(nums []int, k int) int64 {
	n := len(nums)
	var ans int64 = 1 << 62
	for i := 0; i+k <= n; i++ {
		sub := append([]int(nil), nums[i:i+k]...)
		sort.Ints(sub)
		med := sub[k/2]
		var cost int64
		for _, x := range sub {
			d := x - med
			if d < 0 {
				d = -d
			}
			cost += int64(d)
		}
		if cost < ans {
			ans = cost
		}
	}
	return ans
}
