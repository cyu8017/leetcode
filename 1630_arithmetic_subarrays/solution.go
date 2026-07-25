// LeetCode 1630 - Arithmetic Subarrays
// https://leetcode.com/problems/arithmetic-subarrays/

import "sort"

func checkArithmeticSubarrays(nums []int, l []int, r []int) []bool {
	ans := make([]bool, len(l))
	for i := range l {
		a, b := l[i], r[i]
		x := append([]int{}, nums[a:b+1]...)
		sort.Ints(x)
		ok := true
		if len(x) >= 3 {
			diff := x[1] - x[0]
			for j := 2; j < len(x); j++ {
				if x[j]-x[j-1] != diff {
					ok = false
					break
				}
			}
		}
		ans[i] = ok
	}
	return ans
}
