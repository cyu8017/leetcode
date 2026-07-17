// LeetCode 1773 - Count Items Matching a Rule
// https://leetcode.com/problems/count-items-matching-a-rule/

class Solution {
    public int countMatches(String[][] items, String ruleKey, String ruleValue) {
        int idx = ruleKey.equals("type") ? 0 : ruleKey.equals("color") ? 1 : 2;
        int count = 0;
        for (String[] item : items) {
            if (item[idx].equals(ruleValue)) {
                count++;
            }
        }
        return count;
    }
}
