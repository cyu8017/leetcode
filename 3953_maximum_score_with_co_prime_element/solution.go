// LeetCode 3953 - Maximum Score with Co-Prime Element
// https://leetcode.com/problems/maximum-score-with-co-prime-element/

func maxScore(nums []int, maxVal int) int {
	limit := maxVal
	frequency := make([]int, 100001)
	for _, x := range nums {
		frequency[x]++
		if x > limit {
			limit = x
		}
	}
	divisible := make([]int, limit+1)
	for d := 1; d <= limit; d++ {
		for multiple := d; multiple <= limit; multiple += d {
			if multiple < len(frequency) {
				divisible[d] += frequency[multiple]
			}
		}
	}
	badCount := func(x int) int {
		primes := make([]int, 0)
		y := x
		for p := 2; p*p <= y; p++ {
			if y%p == 0 {
				primes = append(primes, p)
				for y%p == 0 {
					y /= p
				}
			}
		}
		if y > 1 {
			primes = append(primes, y)
		}
		bad := 0
		for mask := 1; mask < 1<<len(primes); mask++ {
			product, bits := 1, 0
			for i, p := range primes {
				if mask>>i&1 != 0 {
					product *= p
					bits++
				}
			}
			if bits%2 == 1 {
				bad += divisible[product]
			} else {
				bad -= divisible[product]
			}
		}
		return bad
	}
	best := -len(nums)
	checked := make([]bool, limit+1)
	evaluate := func(x int, exists bool) {
		if checked[x] {
			return
		}
		checked[x] = true
		bad := badCount(x)
		cost := 0
		if exists {
			if x > 1 {
				cost = bad - 1
			}
		} else if bad > 0 {
			cost = bad
		} else {
			cost = 1
		}
		if x-cost > best {
			best = x - cost
		}
	}
	for x := 1; x <= maxVal; x++ {
		evaluate(x, x < len(frequency) && frequency[x] > 0)
	}
	for _, x := range nums {
		evaluate(x, true)
	}
	return best
}