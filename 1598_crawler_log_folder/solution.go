// LeetCode 1598 - Crawler Log Folder
// https://leetcode.com/problems/crawler-log-folder/

func minOperations(logs []string) int {
	depth := 0
	for _, log := range logs {
		if log == "../" {
			if depth > 0 {
				depth--
			}
		} else if log != "./" {
			depth++
		}
	}
	return depth
}
