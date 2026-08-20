// LeetCode 2954 - Count the Number of Infection Sequences
// https://leetcode.com/problems/count-the-number-of-infection-sequences/

func numberOfSequence(n int, sick []int) int {
	const mod = 1_000_000_007
	fact := make([]int, n+1)
	invFact := make([]int, n+1)
	fact[0] = 1
	for i := 1; i <= n; i++ {
		fact[i] = fact[i-1] * i % mod
	}
	modPow := func(a, b int) int {
		res := 1
		for b > 0 {
			if b&1 == 1 {
				res = res * a % mod
			}
			a = a * a % mod
			b >>= 1
		}
		return res
	}
	invFact[n] = modPow(fact[n], mod-2)
	for i := n; i > 0; i-- {
		invFact[i-1] = invFact[i] * i % mod
	}
	comb := func(a, b int) int {
		if b < 0 || b > a {
			return 0
		}
		return fact[a] * invFact[b] % mod * invFact[a-b] % mod
	}
	m := len(sick)
	totalEmpty := n - m
	ans := comb(totalEmpty, totalEmpty)
	// segments
	ans = fact[totalEmpty]
	prev := -1
	for _, s := range sick {
		gap := s - prev - 1
		if prev == -1 {
			ans = ans * invFact[gap] % mod
		} else if gap > 0 {
			ans = ans * invFact[gap] % mod * modPow(2, gap-1) % mod
		}
		prev = s
	}
	gap := n - prev - 1
	ans = ans * invFact[gap] % mod
	return ans
}
