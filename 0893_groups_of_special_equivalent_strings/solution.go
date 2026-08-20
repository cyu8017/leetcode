// LeetCode 0893 - Groups of Special-Equivalent Strings
// https://leetcode.com/problems/groups-of-special-equivalent-strings/

import "sort"

func numSpecialEquivGroups(words []string) int {
	groups := map[string]bool{}
	for _, w := range words {
		even := []byte{}
		odd := []byte{}
		for i := 0; i < len(w); i++ {
			if i%2 == 0 {
				even = append(even, w[i])
			} else {
				odd = append(odd, w[i])
			}
		}
		sort.Slice(even, func(i, j int) bool { return even[i] < even[j] })
		sort.Slice(odd, func(i, j int) bool { return odd[i] < odd[j] })
		groups[string(even)+"|"+string(odd)] = true
	}
	return len(groups)
}
