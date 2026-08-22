// LeetCode 3939 - Count Non Adjacent Subsets in a Rooted Tree
// https://leetcode.com/problems/count-non-adjacent-subsets-in-a-rooted-tree/

func countNonAdjacentSubsets(parent []int, nums []int, k int) int {
	const mod int64 = 1000000007
	n := len(parent)
	children := make([][]int, n)
	for i := 1; i < n; i++ {
		children[parent[i]] = append(children[parent[i]], i)
	}
	dp0, dp1 := make([][]int64, n), make([][]int64, n)
	for u := n - 1; u >= 0; u-- {
		a, b := make([]int64, k), make([]int64, k)
		a[0], b[((nums[u]%k)+k)%k] = 1, 1
		for _, v := range children[u] {
			na, nb := make([]int64, k), make([]int64, k)
			for x := 0; x < k; x++ {
				for y := 0; y < k; y++ {
					allChild := (dp0[v][y] + dp1[v][y]) % mod
					na[(x+y)%k] = (na[(x+y)%k] + a[x]*allChild) % mod
					nb[(x+y)%k] = (nb[(x+y)%k] + b[x]*dp0[v][y]) % mod
				}
			}
			a, b = na, nb
		}
		dp0[u], dp1[u] = a, b
	}
	ans := (dp0[0][0] + dp1[0][0] - 1) % mod
	if ans < 0 {
		ans += mod
	}
	return int(ans)
}