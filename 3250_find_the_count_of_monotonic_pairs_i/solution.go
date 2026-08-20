// LeetCode 3250 - Find the Count of Monotonic Pairs I
// https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/

func countOfPairs(nums []int) int {
	const mod = 1000000007
	n := len(nums)
	dp := make([]int, 51)
	for a := 0; a <= nums[0]; a++ {
		dp[a] = 1
	}
	for i := 1; i < n; i++ {
		ndp := make([]int, 51)
		pref := make([]int, 52)
		for a := 0; a <= 50; a++ {
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
			if maxA1 > 50 {
				maxA1 = 50
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
