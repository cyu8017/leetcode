// LeetCode 2842 - Count K-Subsequences of a String With Maximum Beauty
// https://leetcode.com/problems/count-k-subsequences-of-a-string-with-maximum-beauty/

import "sort"

func countKSubsequencesWithMaxBeauty(s string, k int) int {
	const mod = 1_000_000_007
	freq := [26]int{}
	for i := 0; i < len(s); i++ {
		freq[s[i]-'a']++
	}
	vals := []int{}
	for _, f := range freq {
		if f > 0 {
			vals = append(vals, f)
		}
	}
	if len(vals) < k {
		return 0
	}
	sort.Slice(vals, func(i, j int) bool { return vals[i] > vals[j] })
	threshold := vals[k-1]
	need, avail := 0, 0
	prod := 1
	for _, v := range vals {
		if v > threshold {
			prod = prod * v % mod
			need++
		} else if v == threshold {
			avail++
		}
	}
	remain := k - need
	comb := func(n, r int) int {
		if r < 0 || r > n {
			return 0
		}
		num, den := 1, 1
		for i := 0; i < r; i++ {
			num = num * (n - i) % mod
			den = den * (i + 1) % mod
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
		return num * modPow(den, mod-2) % mod
	}
	prod = prod * comb(avail, remain) % mod
	for i := 0; i < remain; i++ {
		prod = prod * threshold % mod
	}
	return prod
}
