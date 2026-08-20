// LeetCode 2673 - Make Costs of Paths Equal in a Binary Tree
// https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/


func minIncrements(n int, cost []int) int {
	ans := 0
	for i := n/2 - 1; i >= 0; i-- {
		l, r := 2*i+1, 2*i+2
		ans += abs2673(cost[l] - cost[r])
		if cost[l] > cost[r] {
			cost[i] += cost[l]
		} else {
			cost[i] += cost[r]
		}
	}
	return ans
}
func abs2673(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
