// LeetCode 3488 - Closest Equal Element Queries
// https://leetcode.com/problems/closest-equal-element-queries/

func solveQueries(nums []int, queries []int) []int {
	n := len(nums)
	pos := map[int][]int{}
	for i, x := range nums {
		pos[x] = append(pos[x], i)
	}
	ans := make([]int, len(queries))
	for qi, idx := range queries {
		x := nums[idx]
		arr := pos[x]
		if len(arr) == 1 {
			ans[qi] = -1
			continue
		}
		best := n
		for _, p := range arr {
			if p == idx {
				continue
			}
			d := p - idx
			if d < 0 {
				d = -d
			}
			d2 := n - d
			if d2 < d {
				d = d2
			}
			if d < best {
				best = d
			}
		}
		ans[qi] = best
	}
	return ans
}
