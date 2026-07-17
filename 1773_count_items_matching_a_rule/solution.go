// LeetCode 1773 - Count Items Matching a Rule
// https://leetcode.com/problems/count-items-matching-a-rule/

func countMatches(items [][]string, ruleKey string, ruleValue string) int {
    idx := map[string]int{"type": 0, "color": 1, "name": 2}[ruleKey]
    count := 0
    for _, item := range items {
        if item[idx] == ruleValue {
            count++
        }
    }
    return count
}
