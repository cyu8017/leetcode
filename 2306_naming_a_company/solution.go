// LeetCode 2306 - Naming a Company
// https://leetcode.com/problems/naming-a-company/

func distinctNames(ideas []string) int64 {
	groups := make([]map[string]bool, 26)
	for i := range groups {
		groups[i] = map[string]bool{}
	}
	for _, idea := range ideas {
		groups[idea[0]-'a'][idea[1:]] = true
	}
	var ans int64
	for i := 0; i < 26; i++ {
		for j := i + 1; j < 26; j++ {
			overlap := 0
			for s := range groups[i] {
				if groups[j][s] {
					overlap++
				}
			}
			ans += int64(len(groups[i])-overlap) * int64(len(groups[j])-overlap) * 2
		}
	}
	return ans
}
