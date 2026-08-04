// LeetCode 1208 - Get Equal Substrings Within Budget
// https://leetcode.com/problems/get-equal-substrings-within-budget/

class Solution {
    public int equalSubstring(String s, String t, int maxCost) {
        int left = 0, cost = 0, answer = 0;
        for (int right = 0; right < s.length(); right++) {
            cost += Math.abs(s.charAt(right) - t.charAt(right));
            while (cost > maxCost) {
                cost -= Math.abs(s.charAt(left) - t.charAt(left));
                left++;
            }
            answer = Math.max(answer, right - left + 1);
        }
        return answer;
    }
}
