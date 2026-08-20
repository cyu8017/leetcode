// LeetCode 2867 - Count Valid Paths in a Tree
// https://leetcode.com/problems/count-valid-paths-in-a-tree/

func countPaths(n int, edges [][]int) int64 {
	isPrime := make([]bool, n+1)
	for i := 2; i <= n; i++ {
		isPrime[i] = true
	}
	for i := 2; i*i <= n; i++ {
		if isPrime[i] {
			for j := i * i; j <= n; j += i {
				isPrime[j] = false
			}
		}
	}
	g := make([][]int, n+1)
	for _, e := range edges {
		u, v := e[0], e[1]
		g[u] = append(g[u], v)
		g[v] = append(g[v], u)
	}
	parent := make([]int, n+1)
	order := []int{}
	stack := []int{1}
	parent[1] = -1
	for len(stack) > 0 {
		u := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		order = append(order, u)
		for _, v := range g[u] {
			if v != parent[u] {
				parent[v] = u
				stack = append(stack, v)
			}
		}
	}
	size := make([]int, n+1)
	for i := len(order) - 1; i >= 0; i-- {
		u := order[i]
		size[u] = 1
		for _, v := range g[u] {
			if v != parent[u] && !isPrime[v] {
				size[u] += size[v]
			}
		}
	}
	var ans int64
	for u := 1; u <= n; u++ {
		if !isPrime[u] {
			continue
		}
		var pref int64
		for _, v := range g[u] {
			sz := 0
			if !isPrime[v] {
				if parent[v] == u {
					sz = size[v]
				} else {
					// parent side non-prime component
					sz = size[v]
				}
			}
			_ = sz
		}
		comps := []int{}
		for _, v := range g[u] {
			if isPrime[v] {
				continue
			}
			if parent[v] == u {
				comps = append(comps, size[v])
			} else {
				// climb: size of non-prime component containing parent
				comps = append(comps, size[u]-1) // wrong
			}
		}
		// recompute properly via DFS from each prime
	}
	seen := make([]bool, n+1)
	var dfs func(int, int) int
	dfs = func(u, p int) int {
		if isPrime[u] {
			return 0
		}
		sz := 1
		for _, v := range g[u] {
			if v != p {
				sz += dfs(v, u)
			}
		}
		return sz
	}
	ans = 0
	for u := 1; u <= n; u++ {
		if !isPrime[u] || seen[u] {
			continue
		}
		comps := []int{}
		for _, v := range g[u] {
			comps = append(comps, dfs(v, u))
		}
		var total int64
		for _, c := range comps {
			ans += int64(c)
			ans += total * int64(c)
			total += int64(c)
		}
	}
	return ans
}
