// LeetCode 3538 - Merge Operations for Minimum Travel Time
// https://leetcode.com/problems/merge-operations-for-minimum-travel-time/

func minTravelTime(l int, n int, k int, position []int, time []int) int {
	prefix := make([]int, n)
	prefix[0] = time[0]
	for i := 1; i < n; i++ {
		prefix[i] = prefix[i-1] + time[i]
	}
	const inf = int(1e18)
	memo := map[[3]int]int{}
	var dp func(i, skips, last int) int
	dp = func(i, skips, last int) int {
		if i == n-1 {
			if skips == 0 {
				return 0
			}
			return inf
		}
		key := [3]int{i, skips, last}
		if v, ok := memo[key]; ok {
			return v
		}
		rate := prefix[i]
		if last > 0 {
			rate -= prefix[last-1]
		}
		res := inf
		end := n - 1
		if i+skips+1 < end {
			end = i + skips + 1
		}
		for j := i + 1; j <= end; j++ {
			cand := (position[j]-position[i])*rate + dp(j, skips-(j-i-1), i+1)
			if cand < res {
				res = cand
			}
		}
		memo[key] = res
		return res
	}
	_ = l
	return dp(0, k, 0)
}
