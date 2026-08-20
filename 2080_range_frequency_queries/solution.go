// LeetCode 2080 - Range Frequency Queries
// https://leetcode.com/problems/range-frequency-queries/

import "sort"

type RangeFreqQuery struct {
	pos map[int][]int
}

func Constructor(arr []int) RangeFreqQuery {
	pos := map[int][]int{}
	for i, v := range arr {
		pos[v] = append(pos[v], i)
	}
	return RangeFreqQuery{pos: pos}
}

func (this *RangeFreqQuery) Query(left int, right int, value int) int {
	p := this.pos[value]
	l := sort.SearchInts(p, left)
	r := sort.Search(len(p), func(i int) bool { return p[i] > right })
	return r - l
}
