// LeetCode 3343 - Count Number of Balanced Permutations
// https://leetcode.com/problems/count-number-of-balanced-permutations/

func countBalancedPermutations(num string) int {
	const mod = 1000000007
	cnt := [10]int{}
	sum := 0
	for _, c := range num {
		d := int(c - '0')
		cnt[d]++
		sum += d
	}
	if sum%2 != 0 {
		return 0
	}
	n := len(num)
	halfSum := sum / 2
	halfLen := n / 2
	fact := make([]int, n+1)
	invFact := make([]int, n+1)
	fact[0] = 1
	for i := 1; i <= n; i++ {
		fact[i] = fact[i-1] * i % mod
	}
	invFact[n] = modInv3343(fact[n], mod)
	for i := n; i > 0; i-- {
		invFact[i-1] = invFact[i] * i % mod
	}
	// dp[digits used in even positions][sum] - actually positions: first halfLen get even indices? 
	// balanced: sum of digits at even indices == odd indices
	// place halfLen digits in even positions with sum halfSum
	dp := make([][]int, halfLen+1)
	for i := range dp {
		dp[i] = make([]int, halfSum+1)
	}
	dp[0][0] = 1
	for d := 0; d <= 9; d++ {
		if cnt[d] == 0 {
			continue
		}
		ndp := make([][]int, halfLen+1)
		for i := range ndp {
			ndp[i] = make([]int, halfSum+1)
		}
		for used := 0; used <= halfLen; used++ {
			for s := 0; s <= halfSum; s++ {
				if dp[used][s] == 0 {
					continue
				}
				for take := 0; take <= cnt[d] && used+take <= halfLen && s+take*d <= halfSum; take++ {
					ways := dp[used][s] * invFact[take] % mod * invFact[cnt[d]-take] % mod
					ndp[used+take][s+take*d] = (ndp[used+take][s+take*d] + ways) % mod
				}
			}
		}
		dp = ndp
	}
	ans := dp[halfLen][halfSum]
	ans = ans * fact[halfLen] % mod * fact[n-halfLen] % mod
	for d := 0; d <= 9; d++ {
		ans = ans * fact[cnt[d]] % mod // cancel the invFact applied per digit combos? 
	}
	// Fix: standard approach already multiplies inv for choosing counts; then * fact[half]*fact[odd]
	// We applied invFact[take]*invFact[rest] for each digit; need * fact[cnt[d]] once overall? 
	// Recompute simply:
	return countBalancedPermutationsFixed(num)
}

func countBalancedPermutationsFixed(num string) int {
	const mod = 1000000007
	cnt := [10]int{}
	tot := 0
	for _, c := range num {
		cnt[c-'0']++
		tot += int(c - '0')
	}
	if tot%2 != 0 {
		return 0
	}
	n := len(num)
	target := tot / 2
	half := n / 2
	fact := make([]int, n+1)
	invF := make([]int, n+1)
	fact[0] = 1
	for i := 1; i <= n; i++ {
		fact[i] = fact[i-1] * i % mod
	}
	invF[n] = modInv3343(fact[n], mod)
	for i := n; i > 0; i-- {
		invF[i-1] = invF[i] * i % mod
	}
	dp := make([][]int, half+1)
	for i := range dp {
		dp[i] = make([]int, target+1)
	}
	dp[0][0] = 1
	for d := 0; d <= 9; d++ {
		ndp := make([][]int, half+1)
		for i := range ndp {
			ndp[i] = append([]int(nil), dp[i]...)
		}
		for c := 1; c <= cnt[d]; c++ {
			for used := half; used >= c; used-- {
				for s := target; s >= c*d; s-- {
					ndp[used][s] = (ndp[used][s] + dp[used-c][s-c*d]*invF[c]%mod*invF[cnt[d]-c]%mod) % mod
				}
			}
		}
		// also ways taking 0 already in ndp; but for take 0 need invF[0]*invF[cnt]
		for used := 0; used <= half; used++ {
			for s := 0; s <= target; s++ {
				if dp[used][s] != 0 {
					ndp[used][s] = (dp[used][s] * invF[cnt[d]] % mod) // wait this double counts
				}
			}
		}
		_ = ndp
	}
	// Use cleaner enumeration
	return countBalancedClean(num)
}

func countBalancedClean(num string) int {
	const mod = 1000000007
	cnt := [10]int{}
	sum := 0
	for _, c := range num {
		cnt[c-'0']++
		sum += int(c - '0')
	}
	if sum%2 == 1 {
		return 0
	}
	n := len(num)
	halfN, halfS := n/2, sum/2
	fact := make([]int, n+1)
	invF := make([]int, n+1)
	fact[0] = 1
	for i := 1; i <= n; i++ {
		fact[i] = int(int64(fact[i-1]) * int64(i) % mod)
	}
	invF[n] = modInv3343(fact[n], mod)
	for i := n; i > 0; i-- {
		invF[i-1] = int(int64(invF[i]) * int64(i) % mod)
	}
	dp := map[[2]int]int{{0, 0}: 1}
	for d := 0; d <= 9; d++ {
		ndp := map[[2]int]int{}
		for st, ways := range dp {
			used, s := st[0], st[1]
			for take := 0; take <= cnt[d]; take++ {
				nu, ns := used+take, s+take*d
				if nu > halfN || ns > halfS {
					continue
				}
				w := int(int64(ways) * int64(invF[take]) % mod * int64(invF[cnt[d]-take]) % mod)
				ndp[[2]int{nu, ns}] = (ndp[[2]int{nu, ns}] + w) % mod
			}
		}
		dp = ndp
	}
	ans := dp[[2]int{halfN, halfS}]
	ans = int(int64(ans) * int64(fact[halfN]) % mod * int64(fact[n-halfN]) % mod)
	for d := 0; d <= 9; d++ {
		ans = int(int64(ans) * int64(fact[cnt[d]]) % mod)
	}
	return ans
}

func modInv3343(a, mod int) int {
	return modPow3343(a, mod-2, mod)
}
func modPow3343(a, e, mod int) int {
	r := 1
	for e > 0 {
		if e&1 == 1 {
			r = int(int64(r) * int64(a) % int64(mod))
		}
		a = int(int64(a) * int64(a) % int64(mod))
		e >>= 1
	}
	return r
}
