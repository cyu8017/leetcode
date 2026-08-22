// LeetCode 3351 - Sum of Good Subsequences
// https://leetcode.com/problems/sum-of-good-subsequences/

func sumOfGoodSubsequences(nums []int) int {
	const mod = 1000000007
	cnt := map[int]int{}
	sum := map[int]int{}
	ans := 0
	for _, x := range nums {
		c := 1
		s := x
		if cnt[x-1] > 0 {
			c = (c + cnt[x-1]) % mod
			s = (s + sum[x-1] + cnt[x-1]*x%mod) % mod
		}
		if cnt[x+1] > 0 {
			c = (c + cnt[x+1]) % mod
			s = (s + sum[x+1] + cnt[x+1]*x%mod) % mod
		}
		cnt[x] = (cnt[x] + c) % mod
		sum[x] = (sum[x] + s) % mod
		ans = (ans + s) % mod
	}
	return ans
}
