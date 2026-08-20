// LeetCode 2539 - Count the Number of Good Subsequences
// https://leetcode.com/problems/count-the-number-of-good-subsequences/


const MOD2539 = 1000000007

func countGoodSubsequences(s string) int {
	cnt := [26]int{}
	maxf := 0
	for i := 0; i < len(s); i++ {
		cnt[s[i]-'a']++
		if cnt[s[i]-'a'] > maxf {
			maxf = cnt[s[i]-'a']
		}
	}
	fact := make([]int64, maxf+1)
	invFact := make([]int64, maxf+1)
	fact[0] = 1
	for i := 1; i <= maxf; i++ {
		fact[i] = fact[i-1] * int64(i) % MOD2539
	}
	invFact[maxf] = modPow2539(fact[maxf], MOD2539-2)
	for i := maxf; i > 0; i-- {
		invFact[i-1] = invFact[i] * int64(i) % MOD2539
	}
	comb := func(n, k int) int64 {
		if k < 0 || k > n {
			return 0
		}
		return fact[n] * invFact[k] % MOD2539 * invFact[n-k] % MOD2539
	}
	ans := int64(0)
	for k := 1; k <= maxf; k++ {
		ways := int64(1)
		for i := 0; i < 26; i++ {
			if cnt[i] >= k {
				ways = ways * (1 + comb(cnt[i], k)) % MOD2539
			}
		}
		ans = (ans + ways - 1 + MOD2539) % MOD2539
	}
	return int(ans)
}

func modPow2539(a, e int64) int64 {
	res := int64(1)
	for e > 0 {
		if e&1 == 1 {
			res = res * a % MOD2539
		}
		a = a * a % MOD2539
		e >>= 1
	}
	return res
}
