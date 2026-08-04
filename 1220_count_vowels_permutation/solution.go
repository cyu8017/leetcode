// LeetCode 1220 - Count Vowels Permutation
// https://leetcode.com/problems/count-vowels-permutation/

func countVowelPermutation(n int) int {
	const mod = 1000000007
	a, e, i, o, u := 1, 1, 1, 1, 1
	for step := 1; step < n; step++ {
		a, e, i, o, u = (e+i+u)%mod, (a+i)%mod, (e+o)%mod, i, (i+o)%mod
	}
	return (a + e + i + o + u) % mod
}
