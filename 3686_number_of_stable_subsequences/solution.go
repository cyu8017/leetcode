// LeetCode 3686 - Number of Stable Subsequences
// https://leetcode.com/problems/number-of-stable-subsequences/

func countStableSubsequences(nums []int) int {
	const MOD = 1_000_000_007
	// stable: no three consecutive same parity
	// dp0_1, dp0_2: ending with 1/2 odds; dp1_1, dp1_2 ending with 1/2 evens
	var a1, a2, b1, b2 int
	for _, x := range nums {
		if x%2 == 1 {
			na1 := (1 + b1 + b2) % MOD
			na2 := a1
			a1, a2 = (a1+na1)%MOD, (a2+na2)%MOD
		} else {
			nb1 := (1 + a1 + a2) % MOD
			nb2 := b1
			b1, b2 = (b1+nb1)%MOD, (b2+nb2)%MOD
		}
	}
	return (((a1+a2)%MOD + b1) % MOD + b2) % MOD
}
