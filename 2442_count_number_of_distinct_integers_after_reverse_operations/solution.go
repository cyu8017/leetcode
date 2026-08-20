// LeetCode 2442 - Count Number of Distinct Integers After Reverse Operations
// https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

func countDistinctIntegers(nums []int) int {
	seen := map[int]bool{}
	rev := func(x int) int {
		r := 0
		for x > 0 {
			r = r*10 + x%10
			x /= 10
		}
		return r
	}
	for _, x := range nums {
		seen[x] = true
		seen[rev(x)] = true
	}
	return len(seen)
}
