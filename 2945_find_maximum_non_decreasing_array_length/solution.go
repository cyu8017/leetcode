// LeetCode 2945 - Find Maximum Non-decreasing Array Length
// https://leetcode.com/problems/find-maximum-non-decreasing-array-length/

func findMaximumLength(nums []int) int {
	n := len(nums)
	pref := make([]int64, n+1)
	for i := 0; i < n; i++ {
		pref[i+1] = pref[i] + int64(nums[i])
	}
	dp := make([]int, n+1)
	last := make([]int64, n+1)
	type pair struct {
		idx int
		val int64
	}
	dq := []pair{{0, 0}}
	for i := 1; i <= n; i++ {
		for len(dq) > 1 && dq[1].val <= pref[i] {
			dq = dq[1:]
		}
		j := dq[0].idx
		dp[i] = dp[j] + 1
		last[i] = pref[i] - pref[j]
		val := pref[i] + last[i]
		for len(dq) > 0 && dq[len(dq)-1].val >= val {
			dq = dq[:len(dq)-1]
		}
		dq = append(dq, pair{i, val})
	}
	return dp[n]
}
