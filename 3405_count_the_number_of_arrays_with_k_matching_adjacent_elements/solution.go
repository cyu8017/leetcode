// LeetCode 3405 - Count the Number of Arrays With K Matching Adjacent Elements
// https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/

func countGoodArrays(n int, m int, k int) int {
	const mod = 1000000007
	// C(n-1, k) * m * (m-1)^(n-1-k)
	return int(int64(comb3405(n-1, k, mod)) * int64(m) % mod * modPow3405(m-1, n-1-k, mod) % mod)
}

func comb3405(n, k, mod int) int {
	if k < 0 || k > n {
		return 0
	}
	num, den := 1, 1
	for i := 0; i < k; i++ {
		num = int(int64(num) * int64(n-i) % int64(mod))
		den = int(int64(den) * int64(i+1) % int64(mod))
	}
	return int(int64(num) * int64(modPow3405(den, mod-2, mod)) % int64(mod))
}

func modPow3405(a, e, mod int) int {
	if a < 0 {
		a = 0
	}
	r := 1
	a %= mod
	for e > 0 {
		if e&1 == 1 {
			r = int(int64(r) * int64(a) % int64(mod))
		}
		a = int(int64(a) * int64(a) % int64(mod))
		e >>= 1
	}
	return r
}
