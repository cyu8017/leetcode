// LeetCode 2751 - Robot Collisions
// https://leetcode.com/problems/robot-collisions/

import "sort"

func survivedRobotsHealths(positions []int, healths []int, directions string) []int {
	n := len(positions)
	idx := make([]int, n)
	for i := range idx {
		idx[i] = i
	}
	sort.Slice(idx, func(i, j int) bool { return positions[idx[i]] < positions[idx[j]] })
	type robot struct{ i, h int; d byte }
	stack := make([]robot, 0)
	for _, i := range idx {
		cur := robot{i, healths[i], directions[i]}
		for len(stack) > 0 && stack[len(stack)-1].d == 'R' && cur.d == 'L' {
			top := &stack[len(stack)-1]
			if top.h == cur.h {
				stack = stack[:len(stack)-1]
				cur.h = 0
				break
			} else if top.h > cur.h {
				top.h--
				cur.h = 0
				break
			} else {
				cur.h--
				stack = stack[:len(stack)-1]
			}
		}
		if cur.h > 0 {
			stack = append(stack, cur)
		}
	}
	alive := make(map[int]int)
	for _, r := range stack {
		alive[r.i] = r.h
	}
	ans := make([]int, 0)
	for i := 0; i < n; i++ {
		if h, ok := alive[i]; ok {
			ans = append(ans, h)
		}
	}
	return ans
}
