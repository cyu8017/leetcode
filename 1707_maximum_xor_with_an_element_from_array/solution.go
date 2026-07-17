// LeetCode 1707 - Maximum XOR With an Element From Array
// https://leetcode.com/problems/maximum-xor-with-an-element-from-array/

import "sort"

func maximizeXor(nums []int, queries [][]int) []int {
	sort.Ints(nums)
	order := make([]int, len(queries))
	for i := range order {
		order[i] = i
	}
	sort.Slice(order, func(a, b int) bool {
		return queries[order[a]][1] < queries[order[b]][1]
	})

	children := [][2]int{{-1, -1}}
	insert := func(num int) {
		node := 0
		for bit := 31; bit >= 0; bit-- {
			b := (num >> bit) & 1
			if children[node][b] == -1 {
				children[node][b] = len(children)
				children = append(children, [2]int{-1, -1})
			}
			node = children[node][b]
		}
	}

	ans := make([]int, len(queries))
	for i := range ans {
		ans[i] = -1
	}
	added := 0
	for _, qi := range order {
		x, limit := queries[qi][0], queries[qi][1]
		for added < len(nums) && nums[added] <= limit {
			insert(nums[added])
			added++
		}
		if added == 0 {
			continue
		}
		node := 0
		value := 0
		for bit := 31; bit >= 0; bit-- {
			b := (x >> bit) & 1
			want := b ^ 1
			if children[node][want] != -1 {
				value |= 1 << bit
				node = children[node][want]
			} else {
				node = children[node][b]
			}
		}
		ans[qi] = value
	}
	return ans
}
