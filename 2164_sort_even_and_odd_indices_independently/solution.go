// LeetCode 2164 - Sort Even and Odd Indices Independently
// https://leetcode.com/problems/sort-even-and-odd-indices-independently/

import "sort"

func sortEvenOdd(nums []int) []int {
	even, odd := []int{}, []int{}
	for i, x := range nums {
		if i%2 == 0 {
			even = append(even, x)
		} else {
			odd = append(odd, x)
		}
	}
	sort.Ints(even)
	sort.Sort(sort.Reverse(sort.IntSlice(odd)))
	ei, oi := 0, 0
	for i := range nums {
		if i%2 == 0 {
			nums[i] = even[ei]
			ei++
		} else {
			nums[i] = odd[oi]
			oi++
		}
	}
	return nums
}
