// LeetCode 2400 - Number of Ways to Reach a Position After Exactly k Steps
// https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

func numberOfWays(startPos int, endPos int, k int) int {
	const mod = 1000000007
	diff := endPos - startPos
	if diff < 0 {
		diff = -diff
	}
	if diff > k || (k-diff)%2 != 0 {
		return 0
	}
	r := (k + diff) / 2
	return comb(k, r, mod)
}

func comb(n, r, mod int) int {
	if r < 0 || r > n {
		return 0
	}
	num, den := 1, 1
	for i := 0; i < r; i++ {
		num = int(int64(num) * int64(n-i) % int64(mod))
		den = int(int64(den) * int64(i+1) % int64(mod))
	}
	return int(int64(num) * modInverse(den, mod) % int64(mod))
}

func modInverse(a, mod int) int {
	return modPow(a, mod-2, mod)
}

func modPow(a, e, mod int) int {
	res := 1
	a %= mod
	for e > 0 {
		if e&1 == 1 {
			res = int(int64(res) * int64(a) % int64(mod))
		}
		a = int(int64(a) * int64(a) % int64(mod))
		e >>= 1
	}
	return res
}
