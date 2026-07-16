// LeetCode 0047 - Permutations II
// https://leetcode.com/problems/permutations-ii/

import "sort"

func permuteUnique(nums []int) [][]int {
	sort.Ints(nums)
	result := make([][]int, 0)
	path := make([]int, 0, len(nums))
	used := make([]bool, len(nums))

	var backtrack func()
	backtrack = func() {
		if len(path) == len(nums) {
			copyNums := append([]int(nil), path...)
			result = append(result, copyNums)
			return
		}
		for i := 0; i < len(nums); i++ {
			if used[i] {
				continue
			}
			if i > 0 && nums[i] == nums[i-1] && !used[i-1] {
				continue
			}
			used[i] = true
			path = append(path, nums[i])
			backtrack()
			path = path[:len(path)-1]
			used[i] = false
		}
	}

	backtrack()
	return result
}
