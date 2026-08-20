// LeetCode 0839 - Similar String Groups
// https://leetcode.com/problems/similar-string-groups/

func numSimilarGroups(strs []string) int {
	n := len(strs)
	parent := make([]int, n)
	for i := range parent {
		parent[i] = i
	}
	find := func(x int) int {
		for parent[x] != x {
			parent[x] = parent[parent[x]]
			x = parent[x]
		}
		return x
	}
	similar := func(a, b string) bool {
		diff := []int{}
		for i := 0; i < len(a); i++ {
			if a[i] != b[i] {
				diff = append(diff, i)
			}
		}
		return len(diff) == 0 || (len(diff) == 2 && a[diff[0]] == b[diff[1]] && a[diff[1]] == b[diff[0]])
	}
	groups := n
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			if similar(strs[i], strs[j]) {
				pi, pj := find(i), find(j)
				if pi != pj {
					parent[pi] = pj
					groups--
				}
			}
		}
	}
	return groups
}
