// LeetCode 1452 - People Whose List of Favorite Companies Is Not a Subset of Another List
// https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/

func peopleIndexes(favoriteCompanies [][]string) []int {
	sets := make([]map[string]bool, len(favoriteCompanies))
	for i, comps := range favoriteCompanies {
		sets[i] = map[string]bool{}
		for _, c := range comps {
			sets[i][c] = true
		}
	}
	isSubset := func(a, b map[string]bool) bool {
		for k := range a {
			if !b[k] {
				return false
			}
		}
		return true
	}
	var answer []int
	for i, s := range sets {
		ok := true
		for j, t := range sets {
			if i != j && isSubset(s, t) {
				ok = false
				break
			}
		}
		if ok {
			answer = append(answer, i)
		}
	}
	return answer
}
