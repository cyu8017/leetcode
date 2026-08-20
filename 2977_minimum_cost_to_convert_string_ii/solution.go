// LeetCode 2977 - Minimum Cost to Convert String II
// https://leetcode.com/problems/minimum-cost-to-convert-string-ii/

func minimumCost(source string, target string, original []string, changed []string, cost []int) int64 {
	const inf = int64(1) << 60
	ids := map[string]int{}
	id := func(s string) int {
		if v, ok := ids[s]; ok {
			return v
		}
		v := len(ids)
		ids[s] = v
		return v
	}
	for i := range original {
		id(original[i])
		id(changed[i])
	}
	m := len(ids)
	dist := make([][]int64, m)
	for i := range dist {
		dist[i] = make([]int64, m)
		for j := range dist[i] {
			if i == j {
				dist[i][j] = 0
			} else {
				dist[i][j] = inf
			}
		}
	}
	for i := range original {
		u, v := id(original[i]), id(changed[i])
		w := int64(cost[i])
		if w < dist[u][v] {
			dist[u][v] = w
		}
	}
	for k := 0; k < m; k++ {
		for i := 0; i < m; i++ {
			for j := 0; j < m; j++ {
				if dist[i][k]+dist[k][j] < dist[i][j] {
					dist[i][j] = dist[i][k] + dist[k][j]
				}
			}
		}
	}
	n := len(source)
	dp := make([]int64, n+1)
	for i := range dp {
		dp[i] = inf
	}
	dp[0] = 0
	lens := map[int]bool{}
	for s := range ids {
		lens[len(s)] = true
	}
	for i := 0; i < n; i++ {
		if dp[i] >= inf/2 {
			continue
		}
		if source[i] == target[i] {
			if dp[i] < dp[i+1] {
				dp[i+1] = dp[i]
			}
		}
		for L := range lens {
			if i+L > n {
				continue
			}
			ss, tt := source[i:i+L], target[i:i+L]
			u, ok1 := ids[ss]
			v, ok2 := ids[tt]
			if !ok1 || !ok2 {
				continue
			}
			if dist[u][v] < inf/2 {
				cand := dp[i] + dist[u][v]
				if cand < dp[i+L] {
					dp[i+L] = cand
				}
			}
		}
	}
	if dp[n] >= inf/2 {
		return -1
	}
	return dp[n]
}
