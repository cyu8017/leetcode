// LeetCode 0313 - Super Ugly Number
// https://leetcode.com/problems/super-ugly-number/

func nthSuperUglyNumber(n int, primes []int) int {
	ugly := []int{1}
	pointers := make([]int, len(primes))

	for len(ugly) < n {
		nextValues := make([]int, len(primes))
		for index := range primes {
			nextValues[index] = ugly[pointers[index]] * primes[index]
		}
		nextUgly := nextValues[0]
		for _, value := range nextValues[1:] {
			if value < nextUgly {
				nextUgly = value
			}
		}
		ugly = append(ugly, nextUgly)
		for index := range primes {
			if nextUgly == ugly[pointers[index]]*primes[index] {
				pointers[index]++
			}
		}
	}

	return ugly[len(ugly)-1]
}
