// LeetCode 3447 - Assign Elements to Groups With Constraints
// https://leetcode.com/problems/assign-elements-to-groups-with-constraints/

func assignElements(groups []int, elements []int) []int {
	const maxV = 100001
	first := make([]int, maxV)
	for i := range first {
		first[i] = -1
	}
	for i, e := range elements {
		if e < maxV && first[e] == -1 {
			first[e] = i
		}
	}
	ans := make([]int, len(groups))
	for gi, g := range groups {
		best := -1
		for d := 1; d*d <= g; d++ {
			if g%d == 0 {
				if first[d] != -1 && (best == -1 || first[d] < best) {
					best = first[d]
				}
				other := g / d
				if first[other] != -1 && (best == -1 || first[other] < best) {
					best = first[other]
				}
			}
		}
		ans[gi] = best
	}
	return ans
}
