// LeetCode 1175 - Prime Arrangements
// https://leetcode.com/problems/prime-arrangements/

func numPrimeArrangements(n int) int {
	const MOD = 1000000007
	isPrime := func(x int) bool {
		if x < 2 {
			return false
		}
		for d := 2; d*d <= x; d++ {
			if x%d == 0 {
				return false
			}
		}
		return true
	}
	primes := 0
	for i := 1; i <= n; i++ {
		if isPrime(i) {
			primes++
		}
	}
	fact := func(x int) int {
		res := 1
		for i := 2; i <= x; i++ {
			res = res * i % MOD
		}
		return res
	}
	return fact(primes) * fact(n-primes) % MOD
}
