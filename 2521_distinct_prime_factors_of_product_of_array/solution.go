// LeetCode 2521 - Distinct Prime Factors of Product of Array
// https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

func distinctPrimeFactors(nums []int) int {
	set := map[int]bool{}
	for _, x := range nums {
		for p := 2; p*p <= x; p++ {
			if x%p == 0 {
				set[p] = true
				for x%p == 0 {
					x /= p
				}
			}
		}
		if x > 1 {
			set[x] = true
		}
	}
	return len(set)
}
