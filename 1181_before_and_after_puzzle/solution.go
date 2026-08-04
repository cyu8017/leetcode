// LeetCode 1181 - Before and After Puzzle
// https://leetcode.com/problems/before-and-after-puzzle/

import "sort"
import "strings"

func beforeAndAfterPuzzles(phrases []string) []string {
	split := make([][]string, len(phrases))
	for i, p := range phrases {
		split[i] = strings.Fields(p)
	}
	result := map[string]bool{}
	for i := 0; i < len(split); i++ {
		for j := 0; j < len(split); j++ {
			if i == j {
				continue
			}
			if split[i][len(split[i])-1] == split[j][0] {
				merged := append(append([]string{}, split[i]...), split[j][1:]...)
				result[strings.Join(merged, " ")] = true
			}
		}
	}
	ans := make([]string, 0, len(result))
	for s := range result {
		ans = append(ans, s)
	}
	sort.Strings(ans)
	return ans
}
