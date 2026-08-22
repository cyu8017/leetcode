// LeetCode 3973 - Distinct Gate Paths to LCA
// https://leetcode.com/problems/distinct-gate-paths-to-lca/

type gateMatrix3973 [2][2]int64

func gatePathXor(n int, parent []int, gates [][]int, queries [][]int) int {
	const mod int64 = 1000000007
	multiply := func(a, b gateMatrix3973) gateMatrix3973 {
		var c gateMatrix3973
		for i := 0; i < 2; i++ {
			for j := 0; j < 2; j++ {
				for k := 0; k < 2; k++ {
					c[i][j] = (c[i][j] + a[i][k]*b[k][j]) % mod
				}
			}
		}
		return c
	}
	log := 1
	for 1<<log <= n {
		log++
	}
	up := make([][]int, log)
	product := make([][]gateMatrix3973, log)
	for level := 0; level < log; level++ {
		up[level] = make([]int, n)
		product[level] = make([]gateMatrix3973, n)
	}
	children := make([][]int, n)
	for node := 1; node < n; node++ {
		children[parent[node]] = append(children[parent[node]], node)
	}
	depth := make([]int, n)
	order := []int{0}
	for i := 0; i < len(order); i++ {
		u := order[i]
		for _, v := range children[u] {
			depth[v] = depth[u] + 1
			order = append(order, v)
		}
	}
	for u := 0; u < n; u++ {
		up[0][u] = parent[u]
		if u == 0 {
			up[0][u] = 0
		}
		product[0][u] = gateMatrix3973{
			{int64(gates[u][1]), int64(gates[u][2])},
			{int64(gates[u][2]), int64(gates[u][0])},
		}
	}
	for level := 1; level < log; level++ {
		for u := 0; u < n; u++ {
			mid := up[level-1][u]
			up[level][u] = up[level-1][mid]
			product[level][u] = multiply(product[level-1][u], product[level-1][mid])
		}
	}
	liftNode := func(node, distance int) int {
		for level := 0; distance > 0; level++ {
			if distance&1 != 0 {
				node = up[level][node]
			}
			distance >>= 1
		}
		return node
	}
	lca := func(a, b int) int {
		if depth[a] > depth[b] {
			a = liftNode(a, depth[a]-depth[b])
		} else if depth[b] > depth[a] {
			b = liftNode(b, depth[b]-depth[a])
		}
		if a == b {
			return a
		}
		for level := log - 1; level >= 0; level-- {
			if up[level][a] != up[level][b] {
				a, b = up[level][a], up[level][b]
			}
		}
		return up[0][a]
	}
	ways := func(node, card, distance int) int64 {
		vector := [2]int64{}
		vector[card] = 1
		for level := 0; distance > 0; level++ {
			if distance&1 != 0 {
				matrix := product[level][node]
				vector = [2]int64{
					(vector[0]*matrix[0][0] + vector[1]*matrix[1][0]) % mod,
					(vector[0]*matrix[0][1] + vector[1]*matrix[1][1]) % mod,
				}
				node = up[level][node]
			}
			distance >>= 1
		}
		return (vector[0] + vector[1]) % mod
	}
	answer := 0
	for _, query := range queries {
		ancestor := lca(query[0], query[2])
		alice := ways(query[0], query[1], depth[query[0]]-depth[ancestor])
		bob := ways(query[2], query[3], depth[query[2]]-depth[ancestor])
		total := int(alice * bob % mod)
		answer ^= total
	}
	return answer
}