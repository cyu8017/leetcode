// LeetCode 2307 - Check for Contradictions in Equations
// https://leetcode.com/problems/check-for-contradictions-in-equations/

func checkContradictions(equations [][]string, values []float64) bool {
	parent := map[string]string{}
	weight := map[string]float64{}
	var find func(string) string
	find = func(x string) string {
		if _, ok := parent[x]; !ok {
			parent[x] = x
			weight[x] = 1
			return x
		}
		if parent[x] != x {
			p := find(parent[x])
			weight[x] *= weight[parent[x]]
			parent[x] = p
		}
		return parent[x]
	}
	for i, eq := range equations {
		a, b := eq[0], eq[1]
		ra, rb := find(a), find(b)
		if ra == rb {
			if abs(weight[a]/weight[b]-values[i]) > 1e-5 {
				return true
			}
		} else {
			parent[ra] = rb
			weight[ra] = values[i] * weight[b] / weight[a]
		}
	}
	return false
}

func abs(x float64) float64 {
	if x < 0 {
		return -x
	}
	return x
}
