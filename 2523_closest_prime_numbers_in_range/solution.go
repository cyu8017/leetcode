// LeetCode 2523 - Closest Prime Numbers in Range
// https://leetcode.com/problems/closest-prime-numbers-in-range/

func closestPrimes(left int, right int) []int {
	isPrime := make([]bool, right+1)
	for i := 2; i <= right; i++ {
		isPrime[i] = true
	}
	for i := 2; i*i <= right; i++ {
		if isPrime[i] {
			for j := i * i; j <= right; j += i {
				isPrime[j] = false
			}
		}
	}
	primes := []int{}
	for i := left; i <= right; i++ {
		if isPrime[i] {
			primes = append(primes, i)
		}
	}
	if len(primes) < 2 {
		return []int{-1, -1}
	}
	best := []int{primes[0], primes[1]}
	diff := primes[1] - primes[0]
	for i := 1; i+1 < len(primes); i++ {
		d := primes[i+1] - primes[i]
		if d < diff {
			diff = d
			best = []int{primes[i], primes[i+1]}
		}
	}
	return best
}
