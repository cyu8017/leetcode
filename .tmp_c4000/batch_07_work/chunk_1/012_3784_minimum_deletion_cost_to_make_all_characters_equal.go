// LeetCode 3784 - Minimum Deletion Cost To Make All Characters Equal
// https://leetcode.com/problems/minimum-deletion-cost-to-make-all-characters-equal/

func minCost(s string, cost []int) int64 {
	tot := int64(0)
	g := map[byte]int64{}
	for i, v := range cost {
		tot += int64(v)
		g[s[i]] += int64(v)
	}
	ans := tot
	for _, x := range g {
		ans = min(ans, tot-x)
	}
	return ans
}
