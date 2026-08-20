// LeetCode 0805 - Split Array With Same Average
// https://leetcode.com/problems/split-array-with-same-average/

import "sort"

func splitArraySameAverage(nums []int) bool {
	n := len(nums)
	total := 0
	for _, v := range nums {
		total += v
	}
	sort.Ints(nums)
	type key struct{ target, count, index int }
	memo := map[key]bool{}
	var find func(int, int, int) bool
	find = func(target, count, index int) bool {
		k := key{target, count, index}
		if v, ok := memo[k]; ok {
			return v
		}
		if count == 0 {
			return target == 0
		}
		if index == n || count+index > n || target < 0 {
			return false
		}
		ans := find(target-nums[index], count-1, index+1) || find(target, count, index+1)
		memo[k] = ans
		return ans
	}
	for size := 1; size < n; size++ {
		if total*size%n == 0 && find(total*size/n, size, 0) {
			return true
		}
	}
	return false
}
