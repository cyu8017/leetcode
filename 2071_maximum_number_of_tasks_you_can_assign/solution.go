// LeetCode 2071 - Maximum Number of Tasks You Can Assign
// https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/

import "sort"

func maxTaskAssign(tasks []int, workers []int, pills int, strength int) int {
	sort.Ints(tasks)
	sort.Ints(workers)
	can := func(k int) bool {
		if k == 0 {
			return true
		}
		ws := append([]int{}, workers[len(workers)-k:]...)
		p := pills
		for i := k - 1; i >= 0; i-- {
			task := tasks[i]
			if ws[len(ws)-1] >= task {
				ws = ws[:len(ws)-1]
				continue
			}
			if p == 0 {
				return false
			}
			// find weakest worker who can do with pill
			idx := sort.Search(len(ws), func(j int) bool { return ws[j]+strength >= task })
			if idx == len(ws) {
				return false
			}
			ws = append(ws[:idx], ws[idx+1:]...)
			p--
		}
		return true
	}
	lo, hi := 0, len(tasks)
	if len(workers) < hi {
		hi = len(workers)
	}
	for lo < hi {
		mid := (lo + hi + 1) / 2
		if can(mid) {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	return lo
}
