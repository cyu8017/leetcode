// LeetCode 2766 - Relocate Marbles
// https://leetcode.com/problems/relocate-marbles/

import "sort"

func relocateMarbles(nums []int, moveFrom []int, moveTo []int) []int {
	pos := map[int]bool{}
	for _, v := range nums {
		pos[v] = true
	}
	for i := range moveFrom {
		delete(pos, moveFrom[i])
		pos[moveTo[i]] = true
	}
	ans := make([]int, 0, len(pos))
	for k := range pos {
		ans = append(ans, k)
	}
	sort.Ints(ans)
	return ans
}
