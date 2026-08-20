// LeetCode 2507 - Smallest Value After Replacing With Sum of Prime Factors
// https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

func smallestValue(n int) int {
	sumPrimeFactors := func(x int) int {
		s := 0
		for i := 2; i*i <= x; i++ {
			for x%i == 0 {
				s += i
				x /= i
			}
		}
		if x > 1 {
			s += x
		}
		return s
	}
	for {
		s := sumPrimeFactors(n)
		if s == n {
			return n
		}
		n = s
	}
}
