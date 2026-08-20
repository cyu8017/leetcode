// LeetCode 0996 - Number of Squareful Arrays
// https://leetcode.com/problems/number-of-squareful-arrays/

import "math"

func numSquarefulPerms(nums []int) int {
	count := map[int]int{}
	for _, x := range nums {
		count[x]++
	}
	graph := map[int][]int{}
	for a := range count {
		graph[a] = []int{}
	}
	for a := range count {
		for b := range count {
			s := a + b
			r := int(math.Sqrt(float64(s)))
			if r*r == s {
				graph[a] = append(graph[a], b)
			}
		}
	}
	ans := 0
	var dfs func(x, remain int)
	dfs = func(x, remain int) {
		if remain == 0 {
			ans++
			return
		}
		for _, y := range graph[x] {
			if count[y] > 0 {
				count[y]--
				dfs(y, remain-1)
				count[y]++
			}
		}
	}
	for x := range count {
		count[x]--
		dfs(x, len(nums)-1)
		count[x]++
	}
	return ans
}
