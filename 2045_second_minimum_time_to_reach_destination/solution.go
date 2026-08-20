// LeetCode 2045 - Second Minimum Time to Reach Destination
// https://leetcode.com/problems/second-minimum-time-to-reach-destination/

func secondMinimum(n int, edges [][]int, time int, change int) int {
	g := make([][]int, n+1)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], e[1])
		g[e[1]] = append(g[e[1]], e[0])
	}
	dist1 := make([]int, n+1)
	dist2 := make([]int, n+1)
	for i := range dist1 {
		dist1[i] = -1
		dist2[i] = -1
	}
	type node struct{ u, d int }
	q := []node{{1, 0}}
	dist1[1] = 0
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		for _, v := range g[cur.u] {
			nd := cur.d + 1
			if dist1[v] == -1 {
				dist1[v] = nd
				q = append(q, node{v, nd})
			} else if dist2[v] == -1 && nd > dist1[v] {
				dist2[v] = nd
				q = append(q, node{v, nd})
			}
		}
	}
	steps := dist2[n]
	ans := 0
	for i := 0; i < steps; i++ {
		if (ans/change)%2 == 1 {
			ans += change - ans%change
		}
		ans += time
	}
	return ans
}
