// LeetCode 1487 - Making File Names Unique
// https://leetcode.com/problems/making-file-names-unique/

import "fmt"

func getFolderNames(names []string) []string {
	used := map[string]int{}
	ans := make([]string, len(names))
	for i, name := range names {
		candidate := name
		if _, ok := used[name]; ok {
			k := used[name]
			for {
				candidate = fmt.Sprintf("%s(%d)", name, k)
				if _, exists := used[candidate]; !exists {
					break
				}
				k++
			}
			used[name] = k + 1
		}
		used[candidate] = 1
		ans[i] = candidate
	}
	return ans
}
