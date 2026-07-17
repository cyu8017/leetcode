// LeetCode 1773 - Count Items Matching a Rule
// https://leetcode.com/problems/count-items-matching-a-rule/

class Solution {
    fun countMatches(items: List<List<String>>, ruleKey: String, ruleValue: String): Int {
        val idx = when (ruleKey) {
            "type" -> 0
            "color" -> 1
            else -> 2
        }
        return items.count { it[idx] == ruleValue }
    }
}
