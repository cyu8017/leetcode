// LeetCode 1830 - Minimum Number of Operations to Make String Sorted
// https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/

func makeStringSorted(s string) int {
	const mod = 1_000_000_007
	n := len(s)

	fact := make([]int, n+1)
	fact[0] = 1
	for i := 2; i <= n; i++ {
		fact[i] = fact[i-1] * i % mod
	}

	invFact := make([]int, n+1)
	invFact[n] = modPow(fact[n], mod-2, mod)
	for i := n - 1; i >= 0; i-- {
		invFact[i] = invFact[i+1] * (i + 1) % mod
	}

	freq := make([]int, 26)
	for _, ch := range s {
		freq[ch-'a']++
	}

	ans := 0
	for i, ch := range s {
		c := int(ch - 'a')
		for smaller := 0; smaller < c; smaller++ {
			if freq[smaller] == 0 {
				continue
			}
			freq[smaller]--
			ways := fact[n-i-1]
			for _, count := range freq {
				ways = ways * invFact[count] % mod
			}
			ans = (ans + ways) % mod
			freq[smaller]++
		}
		freq[c]--
	}

	return ans
}

func modPow(base, exp, mod int) int {
	result := 1
	base %= mod
	for exp > 0 {
		if exp&1 == 1 {
			result = result * base % mod
		}
		base = base * base % mod
		exp >>= 1
	}
	return result
}
