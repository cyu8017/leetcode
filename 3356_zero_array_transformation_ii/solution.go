// LeetCode 3356 - Zero Array Transformation II
// https://leetcode.com/problems/zero-array-transformation-ii/

func minZeroArray(nums []int, queries [][]int) int {
	n := len(nums)
	ok := func(k int) bool {
		diff := make([]int, n+1)
		for i := 0; i < k; i++ {
			q := queries[i]
			diff[q[0]] += q[2]
			diff[q[1]+1] -= q[2]
		}
		cur := 0
		for i := 0; i < n; i++ {
			cur += diff[i]
			if cur < nums[i] {
				return false
			}
		}
		return true
	}
	if ok(0) {
		return 0
	}
	lo, hi := 1, len(queries)+1
	for lo < hi {
		mid := (lo + hi) / 2
		if mid <= len(queries) && ok(mid) {
			hi = mid
		} else {
			lo = mid + 1
		}
	}
	if lo > len(queries) {
		return -1
	}
	return lo
}
