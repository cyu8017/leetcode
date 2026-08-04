// LeetCode 1982 - Find Array Given Subset Sums
// https://leetcode.com/problems/find-array-given-subset-sums/

import "sort"

func recoverArray(n int, sums []int) []int {
	sort.Ints(sums)
	ans := make([]int, 0, n)
	for round := 0; round < n; round++ {
		d := sums[1] - sums[0]
		count := make(map[int]int)
		for _, x := range sums {
			count[x]++
		}
		without := make([]int, 0, len(sums)/2)
		withD := make([]int, 0, len(sums)/2)
		for _, x := range sums {
			if count[x] == 0 {
				continue
			}
			count[x]--
			count[x+d]--
			without = append(without, x)
			withD = append(withD, x+d)
		}
		hasZero := false
		for _, x := range without {
			if x == 0 {
				hasZero = true
				break
			}
		}
		if hasZero {
			ans = append(ans, d)
			sums = without
		} else {
			ans = append(ans, -d)
			sums = withD
		}
	}
	return ans
}
