// LeetCode 3519 - Count Numbers with Non-Decreasing Digits
// https://leetcode.com/problems/count-numbers-with-non-decreasing-digits/

import "math/big"

func countNumbers(l string, r string, b int) int {
	const MOD = 1_000_000_007
	toDigits := func(s string) []int {
		x := new(big.Int)
		x.SetString(s, 10)
		if x.Sign() == 0 {
			return []int{0}
		}
		var digs []int
		bb := big.NewInt(int64(b))
		zero := big.NewInt(0)
		mod := new(big.Int)
		for x.Cmp(zero) > 0 {
			x.DivMod(x, bb, mod)
			digs = append(digs, int(mod.Int64()))
		}
		for i, j := 0, len(digs)-1; i < j; i, j = i+1, j-1 {
			digs[i], digs[j] = digs[j], digs[i]
		}
		return digs
	}
	countUpto := func(digs []int) int {
		m := len(digs)
		memo := map[[3]int]int{}
		var dfs func(pos, last int, tight bool) int
		dfs = func(pos, last int, tight bool) int {
			if pos == m {
				return 1
			}
			ti := 0
			if tight {
				ti = 1
			}
			key := [3]int{pos, last, ti}
			if v, ok := memo[key]; ok {
				return v
			}
			up := b - 1
			if tight {
				up = digs[pos]
			}
			res := 0
			for d := last; d <= up; d++ {
				res = (res + dfs(pos+1, d, tight && d == up)) % MOD
			}
			memo[key] = res
			return res
		}
		return dfs(0, 0, true)
	}
	dec := func(s string) string {
		x := new(big.Int)
		x.SetString(s, 10)
		x.Sub(x, big.NewInt(1))
		if x.Sign() < 0 {
			return "0"
		}
		return x.String()
	}
	rd := toDigits(r)
	ld := toDigits(dec(l))
	return (countUpto(rd) - countUpto(ld) + MOD) % MOD
}
