// LeetCode 2359 - Find Closest Node to Given Two Nodes
// https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

func closestMeetingNode(edges []int, node1 int, node2 int) int {
	n := len(edges)
	dist := func(start int) []int {
		d := make([]int, n)
		for i := range d {
			d[i] = -1
		}
		cur, step := start, 0
		for cur != -1 && d[cur] == -1 {
			d[cur] = step
			cur = edges[cur]
			step++
		}
		return d
	}
	d1, d2 := dist(node1), dist(node2)
	ans, best := -1, 1<<30
	for i := 0; i < n; i++ {
		if d1[i] == -1 || d2[i] == -1 {
			continue
		}
		mx := d1[i]
		if d2[i] > mx {
			mx = d2[i]
		}
		if mx < best {
			best = mx
			ans = i
		}
	}
	return ans
}
