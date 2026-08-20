// LeetCode 2143 - Choose Numbers From Two Arrays in Range
// https://leetcode.com/problems/choose-numbers-from-two-arrays-in-range/

func countSubranges(nums1 []int, nums2 []int) int {
	const MOD = 1_000_000_007
	n := len(nums1)
	ans := 0
	dp := map[int]int{}
	for i := 0; i < n; i++ {
		ndp := map[int]int{}
		ndp[nums1[i]] = (ndp[nums1[i]] + 1) % MOD
		ndp[-nums2[i]] = (ndp[-nums2[i]] + 1) % MOD
		for diff, cnt := range dp {
			ndp[diff+nums1[i]] = (ndp[diff+nums1[i]] + cnt) % MOD
			ndp[diff-nums2[i]] = (ndp[diff-nums2[i]] + cnt) % MOD
		}
		dp = ndp
		ans = (ans + dp[0]) % MOD
	}
	return ans
}
