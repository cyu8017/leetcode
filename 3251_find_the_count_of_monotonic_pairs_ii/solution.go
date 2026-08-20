// LeetCode 3251 - Find the Count of Monotonic Pairs II
// https://leetcode.com/problems/find-the-count-of-monotonic-pairs-ii/

func countOfPairs(nums []int) int {
	const mod = 1000000007
	n := len(nums)
	maxV := 0
	for _, x := range nums {
		if x > maxV {
			maxV = x
		}
	}
	dp := make([]int, maxV+1)
	for a := 0; a <= nums[0]; a++ {
		dp[a] = 1
	}
	for i := 1; i < n; i++ {
		ndp := make([]int, maxV+1)
		pref := make([]int, maxV+2)
		for a := 0; a <= maxV; a++ {
			pref[a+1] = (pref[a] + dp[a]) % mod
		}
		for a2 := 0; a2 <= nums[i]; a2++ {
			b2 := nums[i] - a2
			maxA1 := a2
			if lim := nums[i-1] - b2; lim < maxA1 {
				maxA1 = lim
			}
			if maxA1 < 0 {
				continue
			}
			if maxA1 > maxV {
				maxA1 = maxV
			}
			ndp[a2] = pref[maxA1+1]
		}
		dp = ndp
	}
	ans := 0
	for _, v := range dp {
		ans = (ans + v) % mod
	}
	return ans
}
