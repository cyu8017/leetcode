// LeetCode 1994 - The Number of Good Subsets
// https://leetcode.com/problems/the-number-of-good-subsets/

func numberOfGoodSubsets(nums []int) int {
	const MOD = 1000000007
	primes := []int{2, 3, 5, 7, 11, 13, 17, 19, 23, 29}
	masks := make([]int, 31)
	for x := 2; x <= 30; x++ {
		m := 0
		y := x
		ok := true
		for i, p := range primes {
			if y%p == 0 {
				if (y/p)%p == 0 {
					ok = false
					break
				}
				m |= 1 << i
				y /= p
			}
		}
		if !ok {
			masks[x] = -1
		} else {
			masks[x] = m
		}
	}
	cnt := make([]int, 31)
	for _, v := range nums {
		cnt[v]++
	}
	dp := make([]int, 1<<len(primes))
	dp[0] = 1
	for x := 2; x <= 30; x++ {
		if cnt[x] == 0 || masks[x] < 0 {
			continue
		}
		m := masks[x]
		for state := (1 << len(primes)) - 1; state >= 0; state-- {
			if state&m != 0 {
				continue
			}
			dp[state|m] = (dp[state|m] + dp[state]*cnt[x]) % MOD
		}
	}
	ans := 0
	for i := 1; i < len(dp); i++ {
		ans = (ans + dp[i]) % MOD
	}
	pow2 := 1
	for i := 0; i < cnt[1]; i++ {
		pow2 = pow2 * 2 % MOD
	}
	return ans * pow2 % MOD
}
