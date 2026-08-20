// LeetCode 0940 - Distinct Subsequences II
// https://leetcode.com/problems/distinct-subsequences-ii/

func distinctSubseqII(s string) int {
	const MOD = 1000000007
	ends := map[byte]int{}
	empty := 1
	for i := 0; i < len(s); i++ {
		ch := s[i]
		total := empty
		for _, v := range ends {
			total = (total + v) % MOD
		}
		ends[ch] = total
	}
	ans := empty
	for _, v := range ends {
		ans = (ans + v) % MOD
	}
	return (ans - 1 + MOD) % MOD
}
