// LeetCode 1916 - Count Ways to Build Rooms in an Ant Colony
// https://leetcode.com/problems/count-ways-to-build-rooms-in-an-ant-colony/

func waysToBuildRooms(prevRoom []int) int {
	const MOD = 1000000007
	n := len(prevRoom)
	children := make([][]int, n)
	for room, prev := range prevRoom {
		if prev != -1 {
			children[prev] = append(children[prev], room)
		}
	}
	fact := make([]int, n+1)
	invFact := make([]int, n+1)
	fact[0] = 1
	for i := 1; i <= n; i++ {
		fact[i] = fact[i-1] * i % MOD
	}
	invFact[n] = modPow1916(fact[n], MOD-2, MOD)
	for i := n; i > 0; i-- {
		invFact[i-1] = invFact[i] * i % MOD
	}
	comb := func(a, b int) int {
		return fact[a] * invFact[b] % MOD * invFact[a-b] % MOD
	}
	var dfs func(node int) (int, int)
	dfs = func(node int) (int, int) {
		size, ways := 0, 1
		for _, child := range children[node] {
			childSize, childWays := dfs(child)
			ways = ways * childWays % MOD * comb(size+childSize, childSize) % MOD
			size += childSize
		}
		return size + 1, ways
	}
	_, ways := dfs(0)
	return ways
}

func modPow1916(base, exp, mod int) int {
	res := 1
	base %= mod
	for exp > 0 {
		if exp&1 == 1 {
			res = res * base % mod
		}
		base = base * base % mod
		exp >>= 1
	}
	return res
}
