// LeetCode 1772 - Sort Features by Popularity
// https://leetcode.com/problems/sort-features-by-popularity/

import (
    "sort"
    "strings"
)

func sortFeatures(features []string, responses []string) []string {
    featureSet := make(map[string]bool, len(features))
    for _, f := range features {
        featureSet[f] = true
    }
    count := make(map[string]int)
    for _, response := range responses {
        seen := make(map[string]bool)
        for _, word := range strings.Fields(response) {
            if featureSet[word] {
                seen[word] = true
            }
        }
        for word := range seen {
            count[word]++
        }
    }
    result := make([]string, len(features))
    copy(result, features)
    sort.SliceStable(result, func(i, j int) bool {
        if count[result[i]] != count[result[j]] {
            return count[result[i]] > count[result[j]]
        }
        return result[i] < result[j]
    })
    return result
}
