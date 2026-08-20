// LeetCode 2930 - Number of Strings Which Can Be Rearranged to Contain Substring
// https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/

func stringCount(n int) int {
	const mod = 1_000_000_007
	modPow := func(a, b int) int {
		res := 1
		a %= mod
		for b > 0 {
			if b&1 == 1 {
				res = res * a % mod
			}
			a = a * a % mod
			b >>= 1
		}
		return res
	}
	if n < 4 {
		return 0
	}
	total := modPow(26, n)
	// inclusion-exclusion missing l,e,e,t constraints
	a := modPow(25, n)
	b := modPow(25, n)
	c := (modPow(25, n) + n%mod*modPow(25, n-1)%mod) % mod // missing 'e' at least twice harder
	// Standard solution:
	// 26^n - C(3,1)*25^n + C(3,1)*24^n + C(3,1)*n*25^(n-1) - ...
	ans := total
	ans = (ans - 3*modPow(25, n)%mod + mod) % mod
	ans = (ans + 3*modPow(24, n)%mod) % mod
	ans = (ans - modPow(23, n) + mod) % mod
	ans = (ans + (n%mod)*modPow(25, n-1)%mod) % mod
	ans = (ans - 2*(n%mod)%mod*modPow(24, n-1)%mod + mod) % mod
	ans = (ans + (n%mod)*modPow(23, n-1)%mod) % mod
	ans = (ans - (n%mod)*((n-1+mod)%mod)%mod*modPow(24, n-2)%mod%mod + mod) % mod
	ans = (ans + (n%mod)*((n-1+mod)%mod)%mod*modPow(23, n-2)%mod) % mod
	_ = a
	_ = b
	_ = c
	return ans
}
