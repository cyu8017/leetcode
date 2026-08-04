// LeetCode 1969 - Minimum Non-Zero Product of the Array Elements
// https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/

func minNonZeroProduct(p int) int {
	const MOD = 1000000007
	mx := (int64(1) << p) - 1
	exp := (int64(1) << (p - 1)) - 1
	return int(mx % MOD * modPow1969(mx-1, exp, MOD) % MOD)
}

func modPow1969(base, exp, mod int64) int64 {
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
