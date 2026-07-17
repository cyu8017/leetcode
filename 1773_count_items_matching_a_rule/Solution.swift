// LeetCode 1773 - Count Items Matching a Rule
// https://leetcode.com/problems/count-items-matching-a-rule/

class Solution {
    func countMatches(_ items: [[String]], _ ruleKey: String, _ ruleValue: String) -> Int {
        let idx: Int
        switch ruleKey {
        case "type":
            idx = 0
        case "color":
            idx = 1
        default:
            idx = 2
        }
        return items.filter { $0[idx] == ruleValue }.count
    }
}
