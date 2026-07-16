// LeetCode 0090 - Subsets II
// https://leetcode.com/problems/subsets-ii/

import "sort"

func subsetsWithDup(nums []int) [][]int {
	sort.Ints(nums)
	result := make([][]int, 0)
	path := make([]int, 0)

	var backtrack func(start int)
	backtrack = func(start int) {
		copyPath := append([]int(nil), path...)
		result = append(result, copyPath)
		for i := start; i < len(nums); i++ {
			if i > start && nums[i] == nums[i-1] {
				continue
			}
			path = append(path, nums[i])
			backtrack(i + 1)
			path = path[:len(path)-1]
		}
	}

	backtrack(0)
	return result
}
