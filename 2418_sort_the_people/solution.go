// LeetCode 2418 - Sort the People
// https://leetcode.com/problems/sort-the-people/

import "sort"

func sortPeople(names []string, heights []int) []string {
	idx := make([]int, len(names))
	for i := range idx {
		idx[i] = i
	}
	sort.Slice(idx, func(i, j int) bool { return heights[idx[i]] > heights[idx[j]] })
	ans := make([]string, len(names))
	for i, id := range idx {
		ans[i] = names[id]
	}
	return ans
}
