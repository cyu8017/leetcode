// LeetCode 2191 - Sort the Jumbled Numbers
// https://leetcode.com/problems/sort-the-jumbled-numbers/

import "sort"

func sortJumbled(mapping []int, nums []int) []int {
	mapVal := func(x int) int {
		if x == 0 {
			return mapping[0]
		}
		digits := []int{}
		for x > 0 {
			digits = append(digits, x%10)
			x /= 10
		}
		res := 0
		for i := len(digits) - 1; i >= 0; i-- {
			res = res*10 + mapping[digits[i]]
		}
		return res
	}
	type pair struct{ mapped, idx, val int }
	arr := make([]pair, len(nums))
	for i, v := range nums {
		arr[i] = pair{mapVal(v), i, v}
	}
	sort.Slice(arr, func(i, j int) bool {
		if arr[i].mapped != arr[j].mapped {
			return arr[i].mapped < arr[j].mapped
		}
		return arr[i].idx < arr[j].idx
	})
	ans := make([]int, len(nums))
	for i, p := range arr {
		ans[i] = p.val
	}
	return ans
}
