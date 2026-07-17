// LeetCode 1808 - Maximize Number of Nice Divisors
// https://leetcode.com/problems/maximize-number-of-nice-divisors/

const mod1808 = 1000000007

func maxNiceDivisors(primeFactors int) int {
	if primeFactors <= 3 {
		return primeFactors
	}
	if primeFactors%3 == 0 {
		return powMod1808(3, primeFactors/3, mod1808)
	}
	if primeFactors%3 == 1 {
		return int(int64(powMod1808(3, primeFactors/3-1, mod1808)) * 4 % mod1808)
	}
	return int(int64(powMod1808(3, primeFactors/3, mod1808)) * 2 % mod1808)
}

func powMod1808(base, exp, mod int) int {
	result := 1
	base %= mod
	for exp > 0 {
		if exp&1 == 1 {
			result = result * base % mod
		}
		base = base * base % mod
		exp >>= 1
	}
	return result
}
