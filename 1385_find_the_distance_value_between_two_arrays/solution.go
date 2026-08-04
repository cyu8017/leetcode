// LeetCode 1385 - Find the Distance Value Between Two Arrays
// https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

import "sort"

func findTheDistanceValue(arr1 []int, arr2 []int, d int) int {
	b := append([]int(nil), arr2...)
	sort.Ints(b)
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	ans := 0
	for _, x := range arr1 {
		i := sort.SearchInts(b, x)
		ok := true
		if i < len(b) && abs(b[i]-x) <= d {
			ok = false
		}
		if i > 0 && abs(b[i-1]-x) <= d {
			ok = false
		}
		if ok {
			ans++
		}
	}
	return ans
}
