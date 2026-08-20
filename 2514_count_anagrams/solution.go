// LeetCode 2514 - Count Anagrams
// https://leetcode.com/problems/count-anagrams/

import "strings"

const MOD = 1000000007

func modPow(a, e int64) int64 {
	res := int64(1)
	a %= MOD
	for e > 0 {
		if e&1 == 1 {
			res = res * a % MOD
		}
		a = a * a % MOD
		e >>= 1
	}
	return res
}

func countAnagrams(s string) int {
	words := strings.Fields(s)
	maxN := 0
	for _, w := range words {
		if len(w) > maxN {
			maxN = len(w)
		}
	}
	fact := make([]int64, maxN+1)
	invFact := make([]int64, maxN+1)
	fact[0] = 1
	for i := 1; i <= maxN; i++ {
		fact[i] = fact[i-1] * int64(i) % MOD
	}
	invFact[maxN] = modPow(fact[maxN], MOD-2)
	for i := maxN; i > 0; i-- {
		invFact[i-1] = invFact[i] * int64(i) % MOD
	}
	ans := int64(1)
	for _, w := range words {
		cnt := [26]int{}
		for i := 0; i < len(w); i++ {
			cnt[w[i]-'a']++
		}
		cur := fact[len(w)]
		for _, c := range cnt {
			cur = cur * invFact[c] % MOD
		}
		ans = ans * cur % MOD
	}
	return int(ans)
}
