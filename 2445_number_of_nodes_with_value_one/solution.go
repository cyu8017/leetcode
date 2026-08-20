// LeetCode 2445 - Number of Nodes With Value One
// https://leetcode.com/problems/number-of-nodes-with-value-one/

func numberOfNodes(n int, queries []int) int {
	flip := make([]int, n+1)
	for _, q := range queries {
		flip[q] ^= 1
	}
	ans := 0
	val := make([]int, n+1)
	for i := 1; i <= n; i++ {
		val[i] = flip[i]
		if i > 1 {
			val[i] ^= val[i/2]
		}
		ans += val[i]
	}
	return ans
}
