// LeetCode 1268 - Search Suggestions System
// https://leetcode.com/problems/search-suggestions-system/

import "sort"
import "strings"

func suggestedProducts(products []string, searchWord string) [][]string {
	sort.Strings(products)
	ans := make([][]string, 0, len(searchWord))
	prefix := ""
	for i := 0; i < len(searchWord); i++ {
		prefix += string(searchWord[i])
		idx := sort.SearchStrings(products, prefix)
		group := []string{}
		for j := idx; j < len(products) && j < idx+3; j++ {
			if strings.HasPrefix(products[j], prefix) {
				group = append(group, products[j])
			}
		}
		ans = append(ans, group)
	}
	return ans
}
