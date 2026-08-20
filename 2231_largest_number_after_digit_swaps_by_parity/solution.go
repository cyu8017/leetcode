// LeetCode 2231 - Largest Number After Digit Swaps by Parity
// https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

import "sort"

func largestInteger(num int) int {
	digits := []int{}
	for x := num; x > 0; x /= 10 {
		digits = append([]int{x % 10}, digits...)
	}
	even, odd := []int{}, []int{}
	for _, d := range digits {
		if d%2 == 0 {
			even = append(even, d)
		} else {
			odd = append(odd, d)
		}
	}
	sort.Sort(sort.Reverse(sort.IntSlice(even)))
	sort.Sort(sort.Reverse(sort.IntSlice(odd)))
	ei, oi := 0, 0
	ans := 0
	for _, d := range digits {
		if d%2 == 0 {
			ans = ans*10 + even[ei]
			ei++
		} else {
			ans = ans*10 + odd[oi]
			oi++
		}
	}
	return ans
}
