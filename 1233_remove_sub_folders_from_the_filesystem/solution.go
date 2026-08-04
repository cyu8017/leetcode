// LeetCode 1233 - Remove Sub-Folders from the Filesystem
// https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/

import "sort"
import "strings"

func removeSubfolders(folder []string) []string {
	sort.Strings(folder)
	ans := []string{}
	for _, path := range folder {
		if len(ans) == 0 || !strings.HasPrefix(path, ans[len(ans)-1]+"/") {
			ans = append(ans, path)
		}
	}
	return ans
}
