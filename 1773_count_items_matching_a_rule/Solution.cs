// LeetCode 1773 - Count Items Matching a Rule
// https://leetcode.com/problems/count-items-matching-a-rule/

using System.Collections.Generic;

public class Solution {
    public int CountMatches(IList<IList<string>> items, string ruleKey, string ruleValue) {
        int idx = ruleKey == "type" ? 0 : ruleKey == "color" ? 1 : 2;
        int count = 0;
        foreach (var item in items) {
            if (item[idx] == ruleValue) {
                count++;
            }
        }
        return count;
    }
}
