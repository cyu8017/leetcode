// LeetCode 3299 - Sum of Consecutive Subsequences
// https://leetcode.com/problems/sum-of-consecutive-subsequences/

func rangeSum(nums []int) int {
	const mod = 1000000007
	n := len(nums)
	// for consecutive subsequences (not necessarily contiguous): values form consecutive integers
	cnt := map[int]int{}
	sum := map[int]int{}
	ans := 0
	for _, x := range nums {
		cL, sL := cnt[x-1], sum[x-1]
		cR, sR := cnt[x+1], sum[x+1]
		c := (1 + cL + cR) % mod
		s := (x + sL + cL*x%mod + sR + cR*x%mod) % mod
		// also connect both sides through x
		if cL > 0 && cR > 0 {
			c = (c + cL*cR%mod) % mod
			s = (s + sL*cR%mod + sR*cL%mod + cL*cR%mod*x%mod) % mod
		}
		cnt[x] = (cnt[x] + c) % mod
		sum[x] = (sum[x] + s) % mod
		ans = (ans + s) % mod
	}
	_ = n
	return ans
}
