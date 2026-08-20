// LeetCode 2322 - Minimum Score After Removals on a Tree
// https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/

func minimumScore(nums []int, edges [][]int) int {
	n := len(nums)
	g := make([][]int, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], e[1])
		g[e[1]] = append(g[e[1]], e[0])
	}
	xor := make([]int, n)
	inT := make([]int, n)
	outT := make([]int, n)
	time := 0
	var dfs func(u, p int)
	dfs = func(u, p int) {
		inT[u] = time
		time++
		xor[u] = nums[u]
		for _, v := range g[u] {
			if v == p {
				continue
			}
			dfs(v, u)
			xor[u] ^= xor[v]
		}
		outT[u] = time
	}
	dfs(0, -1)
	isAncestor := func(a, b int) bool {
		return inT[a] <= inT[b] && outT[b] <= outT[a]
	}
	total := xor[0]
	ans := 1 << 30
	for i := 1; i < n; i++ {
		for j := i + 1; j < n; j++ {
			var a, b, c int
			if isAncestor(i, j) {
				a, b, c = xor[j], xor[i]^xor[j], total^xor[i]
			} else if isAncestor(j, i) {
				a, b, c = xor[i], xor[j]^xor[i], total^xor[j]
			} else {
				a, b, c = xor[i], xor[j], total^xor[i]^xor[j]
			}
			mx := a
			if b > mx {
				mx = b
			}
			if c > mx {
				mx = c
			}
			mn := a
			if b < mn {
				mn = b
			}
			if c < mn {
				mn = c
			}
			if mx-mn < ans {
				ans = mx - mn
			}
		}
	}
	return ans
}
