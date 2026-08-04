// LeetCode 1331 - Rank Transform of an Array
// https://leetcode.com/problems/rank-transform-of-an-array/

import "sort"

func arrayRankTransform(arr []int) []int {
	uniq := append([]int(nil), arr...)
	sort.Ints(uniq)
	rank := map[int]int{}
	r := 1
	for _, v := range uniq {
		if _, ok := rank[v]; !ok {
			rank[v] = r
			r++
		}
	}
	answer := make([]int, len(arr))
	for i, v := range arr {
		answer[i] = rank[v]
	}
	return answer
}
