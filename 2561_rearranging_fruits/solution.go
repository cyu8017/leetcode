// LeetCode 2561 - Rearranging Fruits
// https://leetcode.com/problems/rearranging-fruits/


import "sort"

func minCost(basket1 []int, basket2 []int) int64 {
	freq := map[int]int{}
	mn := int(1<<30)
	for _, x := range basket1 {
		freq[x]++
		if x < mn {
			mn = x
		}
	}
	for _, x := range basket2 {
		freq[x]--
		if x < mn {
			mn = x
		}
	}
	extra := []int{}
	for v, c := range freq {
		if c%2 != 0 {
			return -1
		}
		for i := 0; i < abs2561(c)/2; i++ {
			extra = append(extra, v)
		}
	}
	sort.Ints(extra)
	var ans int64
	for i := 0; i < len(extra)/2; i++ {
		a := int64(extra[i])
		b := int64(2 * mn)
		if a < b {
			ans += a
		} else {
			ans += b
		}
	}
	return ans
}
func abs2561(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
