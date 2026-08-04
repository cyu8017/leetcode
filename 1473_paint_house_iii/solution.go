// LeetCode 1473 - Paint House III
// https://leetcode.com/problems/paint-house-iii/

func minCost(houses []int, cost [][]int, m int, n int, target int) int {
	const inf = int(1e15)
	type key struct{ prev, groups int }
	dp := map[key]int{{0, 0}: 0}
	for i, painted := range houses {
		nxt := map[key]int{}
		colors := []int{}
		if painted != 0 {
			colors = []int{painted}
		} else {
			for c := 1; c <= n; c++ {
				colors = append(colors, c)
			}
		}
		for k, value := range dp {
			for _, color := range colors {
				ng := k.groups
				if color != k.prev {
					ng++
				}
				if ng <= target {
					nv := value
					if painted == 0 {
						nv += cost[i][color-1]
					}
					nk := key{color, ng}
					if v, ok := nxt[nk]; !ok || nv < v {
						nxt[nk] = nv
					}
				}
			}
		}
		dp = nxt
	}
	ans := inf
	for k, v := range dp {
		if k.groups == target && v < ans {
			ans = v
		}
	}
	if ans == inf {
		return -1
	}
	return ans
}
