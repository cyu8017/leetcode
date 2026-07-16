// LeetCode 0491 - Non-decreasing Subsequences
// https://leetcode.com/problems/non-decreasing-subsequences/

import (
	"fmt"
	"sort"
)

func findSubsequences(nums []int) [][]int {
	resultSet := make(map[string][]int)
	var backtrack func(start int, path []int)
	backtrack = func(start int, path []int) {
		if len(path) >= 2 {
			key := encode(path)
			resultSet[key] = append([]int(nil), path...)
		}
		used := map[int]bool{}
		for index := start; index < len(nums); index++ {
			if used[nums[index]] {
				continue
			}
			if len(path) > 0 && nums[index] < path[len(path)-1] {
				continue
			}
			used[nums[index]] = true
			path = append(path, nums[index])
			backtrack(index+1, path)
			path = path[:len(path)-1]
		}
	}
	backtrack(0, nil)

	result := make([][]int, 0, len(resultSet))
	for _, sequence := range resultSet {
		result = append(result, sequence)
	}
	sort.Slice(result, func(i, j int) bool {
		left := result[i]
		right := result[j]
		minLen := len(left)
		if len(right) < minLen {
			minLen = len(right)
		}
		for index := 0; index < minLen; index++ {
			if left[index] != right[index] {
				return left[index] < right[index]
			}
		}
		return len(left) < len(right)
	})
	return result
}

func encode(path []int) string {
	parts := make([]interface{}, len(path))
	for index, value := range path {
		parts[index] = value
	}
	return fmt.Sprint(parts...)
}
