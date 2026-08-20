// LeetCode 2101 - Detonate the Maximum Bombs
// https://leetcode.com/problems/detonate-the-maximum-bombs/

func maximumDetonation(bombs [][]int) int {
	n := len(bombs)
	g := make([][]int, n)
	for i := 0; i < n; i++ {
		x1, y1, r1 := bombs[i][0], bombs[i][1], bombs[i][2]
		for j := 0; j < n; j++ {
			if i == j {
				continue
			}
			dx := int64(bombs[j][0] - x1)
			dy := int64(bombs[j][1] - y1)
			if dx*dx+dy*dy <= int64(r1)*int64(r1) {
				g[i] = append(g[i], j)
			}
		}
	}
	ans := 0
	for i := 0; i < n; i++ {
		vis := make([]bool, n)
		q := []int{i}
		vis[i] = true
		cnt := 0
		for len(q) > 0 {
			u := q[0]
			q = q[1:]
			cnt++
			for _, v := range g[u] {
				if !vis[v] {
					vis[v] = true
					q = append(q, v)
				}
			}
		}
		if cnt > ans {
			ans = cnt
		}
	}
	return ans
}
