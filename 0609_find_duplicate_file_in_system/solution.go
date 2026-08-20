// LeetCode 0609 - Find Duplicate File in System
// https://leetcode.com/problems/find-duplicate-file-in-system/

import "strings"

func findDuplicate(paths []string) [][]string {
	contentToPaths := map[string][]string{}
	for _, entry := range paths {
		parts := strings.Split(entry, " ")
		directory := parts[0]
		for _, fileInfo := range parts[1:] {
			idx := strings.Index(fileInfo, "(")
			name := fileInfo[:idx]
			content := fileInfo[idx+1 : len(fileInfo)-1]
			contentToPaths[content] = append(contentToPaths[content], directory+"/"+name)
		}
	}
	result := [][]string{}
	for _, group := range contentToPaths {
		if len(group) > 1 {
			result = append(result, group)
		}
	}
	return result
}
