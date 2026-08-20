// LeetCode 0721 - Accounts Merge
// https://leetcode.com/problems/accounts-merge/

import "sort"

func accountsMerge(accounts [][]string) [][]string {
	parent := map[string]string{}
	emailName := map[string]string{}
	var find func(x string) string
	find = func(x string) string {
		for parent[x] != x {
			parent[x] = parent[parent[x]]
			x = parent[x]
		}
		return x
	}
	union := func(a, b string) {
		parent[find(a)] = find(b)
	}
	for _, account := range accounts {
		name := account[0]
		first := account[1]
		for _, email := range account[1:] {
			if _, ok := parent[email]; !ok {
				parent[email] = email
			}
			emailName[email] = name
			union(first, email)
		}
	}
	groups := map[string][]string{}
	for email := range parent {
		root := find(email)
		groups[root] = append(groups[root], email)
	}
	result := [][]string{}
	for _, emails := range groups {
		sort.Strings(emails)
		row := append([]string{emailName[emails[0]]}, emails...)
		result = append(result, row)
	}
	return result
}
