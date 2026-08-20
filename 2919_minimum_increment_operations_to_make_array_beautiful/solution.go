// LeetCode 2919 - Minimum Increment Operations to Make Array Beautiful
// https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/

func minIncrementOperations(nums []int, k int) int64 {
	n := len(nums)
	var a, b, c int64 // dp for ending positions
	const inf = int64(1) << 60
	a, b, c = 0, 0, 0
	for i := 0; i < n; i++ {
		need := int64(0)
		if nums[i] < k {
			need = int64(k - nums[i])
		}
		na := need + min64(a, min64(b, c))
		a, b, c = b, c, na
		if i < 2 {
			// first two can be free for "beautiful from index 2"
		}
	}
	// proper: for each window of 3, at least one >= k
	dp0, dp1, dp2 := int64(0), int64(0), int64(0)
	for i := 0; i < n; i++ {
		cost := int64(0)
		if nums[i] < k {
			cost = int64(k - nums[i])
		}
		nd0 := cost + min64(dp0, min64(dp1, dp2))
		dp0, dp1, dp2 = dp1, dp2, nd0
	}
	return min64(dp0, min64(dp1, dp2))
}

func min64(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}
