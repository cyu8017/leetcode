// LeetCode 2602 - Minimum Operations to Make All Array Elements Equal
// https://leetcode.com/problems/minimum-operations-to-make-all-array-elements-equal/


import "sort"
func minOperations(nums []int, queries []int) []int64 {
	sort.Ints(nums)
	n := len(nums)
	pref := make([]int64, n+1)
	for i, x := range nums {
		pref[i+1] = pref[i] + int64(x)
	}
	ans := make([]int64, len(queries))
	for qi, q := range queries {
		i := sort.SearchInts(nums, q)
		left := int64(q)*int64(i) - pref[i]
		right := pref[n] - pref[i] - int64(q)*int64(n-i)
		ans[qi] = left + right
	}
	return ans
}
