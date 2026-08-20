// LeetCode 2851 - String Transformation
// https://leetcode.com/problems/string-transformation/

import "strings"

func numberOfWays(s string, t string, k int) int {
	const mod = 1_000_000_007
	n := len(s)
	ss := s + s
	if !strings.Contains(ss[:2*n-1], t) {
		return 0
	}
	// count rotations equal to t
	cnt := 0
	for i := 0; i < n; i++ {
		if ss[i:i+n] == t {
			cnt++
		}
	}
	modPow := func(a, b int) int {
		res := 1
		a %= mod
		for b > 0 {
			if b&1 == 1 {
				res = res * a % mod
			}
			a = a * a % mod
			b >>= 1
		}
		return res
	}
	// dp: f(k)= ways end at same rotation, g(k)= other
	// After k ops: (n-1)^k total sequences; matrix formula
	same := 0
	if s == t {
		same = 1
	}
	pk := modPow(n-1, k)
	invn := modPow(n, mod-2)
	// ways to be at specific rotation: ((n-1)^k + (n-1)*(-1)^k)/n if start same target?
	sign := 1
	if k%2 == 1 {
		sign = mod - 1
	}
	waysSame := (pk + (n-1)%mod*sign%mod) % mod * invn % mod
	waysDiff := (pk - sign + mod) % mod * invn % mod
	if same == 1 {
		return waysSame
	}
	return waysDiff * cnt % mod
}
