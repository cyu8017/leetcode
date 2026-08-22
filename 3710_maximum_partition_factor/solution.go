// LeetCode 3710 - Maximum Partition Factor
// https://leetcode.com/problems/maximum-partition-factor/

func maxPartitionFactor(points [][]int) int {
	n := len(points)
	if n == 2 {
		return 0
	}
	dist := func(i, j int) int {
		dx := points[i][0] - points[j][0]
		dy := points[i][1] - points[j][1]
		if dx < 0 {
			dx = -dx
		}
		if dy < 0 {
			dy = -dy
		}
		return dx + dy
	}
	ok := func(d int) bool {
		g := make([][]int, n)
		for i := 0; i < n; i++ {
			for j := i + 1; j < n; j++ {
				if dist(i, j) < d {
					g[i] = append(g[i], j)
					g[j] = append(g[j], i)
				}
			}
		}
		color := make([]int, n)
		for i := range color {
			color[i] = -1
		}
		for i := 0; i < n; i++ {
			if color[i] != -1 {
				continue
			}
			q := []int{i}
			color[i] = 0
			for len(q) > 0 {
				u := q[0]
				q = q[1:]
				for _, v := range g[u] {
					if color[v] == -1 {
						color[v] = color[u] ^ 1
						q = append(q, v)
					} else if color[v] == color[u] {
						return false
					}
				}
			}
		}
		return true
	}
	lo, hi := 0, 0
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if dist(i, j) > hi {
				hi = dist(i, j)
			}
		}
	}
	for lo < hi {
		mid := (lo + hi + 1) / 2
		if ok(mid) {
			lo = mid
		} else {
			hi = mid - 1
		}
	}
	return lo
}
