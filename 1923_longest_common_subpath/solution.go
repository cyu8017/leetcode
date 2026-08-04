// LeetCode 1923 - Longest Common Subpath
// https://leetcode.com/problems/longest-common-subpath/

func longestCommonSubpath(n int, paths [][]int) int {
	const BASE1, MOD1 = 911382323, 1000000007
	const BASE2, MOD2 = 972663749, 1000000009

	modPow := func(base, exp, mod int) int {
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

	hasCommon := func(length int) bool {
		if length == 0 {
			return true
		}
		var common map[[2]int]struct{}
		pow1 := modPow(BASE1, length, MOD1)
		pow2 := modPow(BASE2, length, MOD2)
		for _, path := range paths {
			if len(path) < length {
				return false
			}
			h1, h2 := 0, 0
			seen := make(map[[2]int]struct{})
			for i, city := range path {
				h1 = (h1*BASE1 + city + 1) % MOD1
				h2 = (h2*BASE2 + city + 1) % MOD2
				if i >= length {
					h1 = (h1 - (path[i-length]+1)*pow1%MOD1 + MOD1) % MOD1
					h2 = (h2 - (path[i-length]+1)*pow2%MOD2 + MOD2) % MOD2
				}
				if i >= length-1 {
					seen[[2]int{h1, h2}] = struct{}{}
				}
			}
			if common == nil {
				common = seen
			} else {
				next := make(map[[2]int]struct{})
				for k := range common {
					if _, ok := seen[k]; ok {
						next[k] = struct{}{}
					}
				}
				common = next
			}
			if len(common) == 0 {
				return false
			}
		}
		return true
	}

	hi := len(paths[0])
	for _, p := range paths {
		if len(p) < hi {
			hi = len(p)
		}
	}
	lo := 0
	for lo < hi {
		mid := (lo + hi + 1) / 2
		if hasCommon(mid) {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	return lo
}
