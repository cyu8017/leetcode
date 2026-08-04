// LeetCode 1922 - Count Good Numbers
// https://leetcode.com/problems/count-good-numbers/

func countGoodNumbers(n int64) int {
	const MOD = 1000000007
	return int(modPow1922(5, (n+1)/2, MOD) * modPow1922(4, n/2, MOD) % MOD)
}

func modPow1922(base, exp, mod int64) int64 {
	var res int64 = 1
	base %= mod
	for exp > 0 {
		if exp&1 == 1 {
			res = res * base % mod
		}
		base = base * base % mod
		exp >>= 1
	}
	return res
}
