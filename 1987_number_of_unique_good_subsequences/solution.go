// LeetCode 1987 - Number of Unique Good Subsequences
// https://leetcode.com/problems/number-of-unique-good-subsequences/

func numberOfUniqueGoodSubsequences(binary string) int {
	const MOD = 1000000007
	ends0, ends1 := 0, 0
	has0 := false
	for i := 0; i < len(binary); i++ {
		if binary[i] == '0' {
			has0 = true
			ends0 = (ends0 + ends1) % MOD
		} else {
			ends1 = (ends0 + ends1 + 1) % MOD
		}
	}
	ans := (ends0 + ends1) % MOD
	if has0 {
		ans = (ans + 1) % MOD
	}
	return ans
}
