// LeetCode 1621 - Number of Sets of K Non-Overlapping Line Segments
// https://leetcode.com/problems/number-of-sets-of-k-non-overlapping-line-segments/

func numberOfSets(n int, k int) int {
	const mod = 1000000007
	return comb1621(n+k-1, 2*k, mod)
}

func comb1621(n, r, mod int) int {
	if r < 0 || r > n {
		return 0
	}
	if r > n-r {
		r = n - r
	}
	num, den := 1, 1
	for i := 0; i < r; i++ {
		num = num * (n - i) % mod
		den = den * (i + 1) % mod
	}
	return num * modInverse1621(den, mod) % mod
}

func modInverse1621(a, mod int) int {
	return modPow1621(a, mod-2, mod)
}

func modPow1621(base, exp, mod int) int {
	res := 1
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
