// LeetCode 2171 - Removing Minimum Number of Magic Beans
// https://leetcode.com/problems/removing-minimum-number-of-magic-beans/

import "sort"

func minimumRemoval(beans []int) int64 {
	sort.Ints(beans)
	n := len(beans)
	var sum int64
	for _, b := range beans {
		sum += int64(b)
	}
	ans := sum
	for i, b := range beans {
		remain := int64(n-i) * int64(b)
		if sum-remain < ans {
			ans = sum - remain
		}
	}
	return ans
}
