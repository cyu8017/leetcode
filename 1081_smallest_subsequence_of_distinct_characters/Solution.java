// LeetCode 1081 - Smallest Subsequence of Distinct Characters
// https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

class Solution {
    public String smallestSubsequence(String s) {
        int[] last = new int[26];
        for (int i = 0; i < s.length(); i++) {
            last[s.charAt(i) - 'a'] = i;
        }
        StringBuilder stack = new StringBuilder();
        boolean[] used = new boolean[26];
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (used[ch - 'a']) {
                continue;
            }
            while (stack.length() > 0
                    && ch < stack.charAt(stack.length() - 1)
                    && last[stack.charAt(stack.length() - 1) - 'a'] > i) {
                char top = stack.charAt(stack.length() - 1);
                stack.deleteCharAt(stack.length() - 1);
                used[top - 'a'] = false;
            }
            stack.append(ch);
            used[ch - 'a'] = true;
        }
        return stack.toString();
    }
}
