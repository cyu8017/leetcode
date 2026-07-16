// LeetCode 0049 - Group Anagrams
// https://leetcode.com/problems/group-anagrams/

import "sort"

func groupAnagrams(strs []string) [][]string {
	groups := make(map[string][]string)

	for _, word := range strs {
		chars := []byte(word)
		sort.Slice(chars, func(i, j int) bool { return chars[i] < chars[j] })
		key := string(chars)
		groups[key] = append(groups[key], word)
	}

	result := make([][]string, 0, len(groups))
	for _, group := range groups {
		sort.Strings(group)
		result = append(result, group)
	}
	sort.Slice(result, func(i, j int) bool {
		return minGroupIndex(strs, result[i]) > minGroupIndex(strs, result[j])
	})
	return result
}

func minGroupIndex(strs []string, group []string) int {
	min := len(strs)
	for _, word := range group {
		for i, candidate := range strs {
			if candidate == word && i < min {
				min = i
				break
			}
		}
	}
	return min
}
