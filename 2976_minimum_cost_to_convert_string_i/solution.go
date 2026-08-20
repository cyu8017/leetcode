// LeetCode 2976 - Minimum Cost to Convert String I
// https://leetcode.com/problems/minimum-cost-to-convert-string-i/

func minimumCost(source string, target string, original []string, changed []string, cost []int) int64 {
	const inf = int64(1) << 60
	dist := make([][]int64, 26)
	for i := range dist {
		dist[i] = make([]int64, 26)
		for j := range dist[i] {
			if i == j {
				dist[i][j] = 0
			} else {
				dist[i][j] = inf
			}
		}
	}
	for i := range original {
		u := int(original[i][0] - 'a')
		v := int(changed[i][0] - 'a')
		w := int64(cost[i])
		if w < dist[u][v] {
			dist[u][v] = w
		}
	}
	for k := 0; k < 26; k++ {
		for i := 0; i < 26; i++ {
			for j := 0; j < 26; j++ {
				if dist[i][k]+dist[k][j] < dist[i][j] {
					dist[i][j] = dist[i][k] + dist[k][j]
				}
			}
		}
	}
	var ans int64
	for i := 0; i < len(source); i++ {
		a, b := int(source[i]-'a'), int(target[i]-'a')
		if dist[a][b] >= inf/2 {
			return -1
		}
		ans += dist[a][b]
	}
	return ans
}
