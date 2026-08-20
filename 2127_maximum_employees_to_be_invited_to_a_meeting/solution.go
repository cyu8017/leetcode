// LeetCode 2127 - Maximum Employees to Be Invited to a Meeting
// https://leetcode.com/problems/maximum-employees-to-be-invited-to-a-meeting/

func maximumInvitations(favorite []int) int {
	n := len(favorite)
	indeg := make([]int, n)
	for _, f := range favorite {
		indeg[f]++
	}
	depth := make([]int, n)
	for i := range depth {
		depth[i] = 1
	}
	q := []int{}
	for i := 0; i < n; i++ {
		if indeg[i] == 0 {
			q = append(q, i)
		}
	}
	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		v := favorite[u]
		if depth[u]+1 > depth[v] {
			depth[v] = depth[u] + 1
		}
		indeg[v]--
		if indeg[v] == 0 {
			q = append(q, v)
		}
	}
	pairSum, maxCycle := 0, 0
	vis := make([]bool, n)
	for i := 0; i < n; i++ {
		if indeg[i] == 0 || vis[i] {
			continue
		}
		// cycle
		u := i
		lenCycle := 0
		for !vis[u] {
			vis[u] = true
			u = favorite[u]
			lenCycle++
		}
		if lenCycle == 2 {
			pairSum += depth[i] + depth[favorite[i]]
		} else if lenCycle > maxCycle {
			maxCycle = lenCycle
		}
	}
	if pairSum > maxCycle {
		return pairSum
	}
	return maxCycle
}
