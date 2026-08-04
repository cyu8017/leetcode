// LeetCode 1366 - Rank Teams by Votes
// https://leetcode.com/problems/rank-teams-by-votes/

import "sort"

func rankTeams(votes []string) string {
	m := len(votes[0])
	count := map[byte][]int{}
	for i := 0; i < m; i++ {
		c := votes[0][i]
		count[c] = make([]int, m)
	}
	for _, v := range votes {
		for i := 0; i < len(v); i++ {
			count[v[i]][i]++
		}
	}
	teams := make([]byte, 0, m)
	for c := range count {
		teams = append(teams, c)
	}
	sort.Slice(teams, func(i, j int) bool {
		a, b := count[teams[i]], count[teams[j]]
		for k := 0; k < m; k++ {
			if a[k] != b[k] {
				return a[k] > b[k]
			}
		}
		return teams[i] < teams[j]
	})
	return string(teams)
}
