// LeetCode 2959 - Number of Possible Sets of Closing Branches
// https://leetcode.com/problems/number-of-possible-sets-of-closing-branches/

func numberOfSets(n int, maxDistance int, roads [][]int) int {
	ans := 0
	for mask := 0; mask < (1 << n); mask++ {
		dist := make([][]int, n)
		for i := 0; i < n; i++ {
			dist[i] = make([]int, n)
			for j := 0; j < n; j++ {
				if i == j {
					dist[i][j] = 0
				} else {
					dist[i][j] = 1 << 29
				}
			}
		}
		for _, r := range roads {
			u, v, w := r[0], r[1], r[2]
			if mask&(1<<u) != 0 && mask&(1<<v) != 0 {
				if w < dist[u][v] {
					dist[u][v] = w
					dist[v][u] = w
				}
			}
		}
		for k := 0; k < n; k++ {
			if mask&(1<<k) == 0 {
				continue
			}
			for i := 0; i < n; i++ {
				if mask&(1<<i) == 0 {
					continue
				}
				for j := 0; j < n; j++ {
					if mask&(1<<j) == 0 {
						continue
					}
					if dist[i][k]+dist[k][j] < dist[i][j] {
						dist[i][j] = dist[i][k] + dist[k][j]
					}
				}
			}
		}
		ok := true
		for i := 0; i < n && ok; i++ {
			if mask&(1<<i) == 0 {
				continue
			}
			for j := 0; j < n; j++ {
				if mask&(1<<j) == 0 {
					continue
				}
				if dist[i][j] > maxDistance {
					ok = false
					break
				}
			}
		}
		if ok {
			ans++
		}
	}
	return ans
}
