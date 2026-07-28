// LeetCode 1057 - Campus Bikes
// https://leetcode.com/problems/campus-bikes/

import "sort"

func assignBikes(workers [][]int, bikes [][]int) []int {
	type triple struct{ d, w, b int }
	triples := make([]triple, 0, len(workers)*len(bikes))
	for w, worker := range workers {
		for b, bike := range bikes {
			d := abs1057(worker[0]-bike[0]) + abs1057(worker[1]-bike[1])
			triples = append(triples, triple{d, w, b})
		}
	}
	sort.Slice(triples, func(i, j int) bool {
		if triples[i].d != triples[j].d {
			return triples[i].d < triples[j].d
		}
		if triples[i].w != triples[j].w {
			return triples[i].w < triples[j].w
		}
		return triples[i].b < triples[j].b
	})
	ans := make([]int, len(workers))
	for i := range ans {
		ans[i] = -1
	}
	usedBikes := make([]bool, len(bikes))
	assigned := 0
	for _, t := range triples {
		if ans[t.w] == -1 && !usedBikes[t.b] {
			ans[t.w] = t.b
			usedBikes[t.b] = true
			assigned++
			if assigned == len(workers) {
				break
			}
		}
	}
	return ans
}

func abs1057(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
