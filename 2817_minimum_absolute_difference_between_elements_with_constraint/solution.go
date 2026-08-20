// LeetCode 2817 - Minimum Absolute Difference Between Elements With Constraint
// https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/

import "sort"

func minAbsoluteDifference(nums []int, x int) int {
	if x == 0 {
		ans := int(^uint(0) >> 1)
		for i := 1; i < len(nums); i++ {
			d := nums[i] - nums[i-1]
			if d < 0 {
				d = -d
			}
			if d < ans {
				ans = d
			}
		}
		return ans
	}
	ans := int(^uint(0) >> 1)
	arr := []int{}
	for i := x; i < len(nums); i++ {
		// insert nums[i-x]
		v := nums[i-x]
		pos := sort.SearchInts(arr, v)
		arr = append(arr, 0)
		copy(arr[pos+1:], arr[pos:])
		arr[pos] = v
		cur := nums[i]
		p := sort.SearchInts(arr, cur)
		if p < len(arr) {
			d := arr[p] - cur
			if d < ans {
				ans = d
			}
		}
		if p > 0 {
			d := cur - arr[p-1]
			if d < ans {
				ans = d
			}
		}
	}
	return ans
}
