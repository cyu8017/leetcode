// LeetCode 3489 - Zero Array Transformation IV
// https://leetcode.com/problems/zero-array-transformation-iv/

func minZeroArray(nums []int, queries [][]int) int {
	n := len(nums)
	ok := func(k int) bool {
		for i := 0; i < n; i++ {
			if nums[i] == 0 {
				continue
			}
			// can we form nums[i] using subset of query values covering i among first k?
			vals := []int{}
			for q := 0; q < k; q++ {
				l, r, v := queries[q][0], queries[q][1], queries[q][2]
				if l <= i && i <= r {
					vals = append(vals, v)
				}
			}
			if !canSubsetSum(vals, nums[i]) {
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

func canSubsetSum(vals []int, target int) bool {
	if target == 0 {
		return true
	}
	dp := make([]bool, target+1)
	dp[0] = true
	for _, v := range vals {
		for s := target; s >= v; s-- {
			if dp[s-v] {
				dp[s] = true
			}
		}
	}
	return dp[target]
}
