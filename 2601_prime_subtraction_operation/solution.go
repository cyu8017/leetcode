// LeetCode 2601 - Prime Subtraction Operation
// https://leetcode.com/problems/prime-subtraction-operation/


func primeSubOperation(nums []int) bool {
	maxV := 0
	for _, x := range nums {
		if x > maxV {
			maxV = x
		}
	}
	isP := make([]bool, maxV+1)
	for i := 2; i <= maxV; i++ {
		isP[i] = true
	}
	for i := 2; i*i <= maxV; i++ {
		if isP[i] {
			for j := i * i; j <= maxV; j += i {
				isP[j] = false
			}
		}
	}
	primes := []int{}
	for i := 2; i <= maxV; i++ {
		if isP[i] {
			primes = append(primes, i)
		}
	}
	prev := 0
	for _, x := range nums {
		if x <= prev {
			return false
		}
		// largest prime p such that x-p > prev
		best := x
		for _, p := range primes {
			if p >= x {
				break
			}
			if x-p > prev {
				best = x - p
			}
		}
		prev = best
	}
	return true
}
