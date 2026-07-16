// LeetCode 0368 - Largest Divisible Subset
// https://leetcode.com/problems/largest-divisible-subset/

import "sort"

func largestDivisibleSubset(nums []int) []int {
	sort.Ints(nums)
	chains := make(map[int][]int, len(nums))
	best := make([]int, 0)

	for _, num := range nums {
		chains[num] = []int{num}
		for prev, chain := range chains {
			if prev < num && num%prev == 0 && len(chain)+1 > len(chains[num]) {
				next := append([]int(nil), chain...)
				next = append(next, num)
				chains[num] = next
			}
		}
		if len(chains[num]) > len(best) {
			best = chains[num]
		}
	}

	return best
}
