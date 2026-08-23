// LeetCode 3816 - Lexicographically Smallest String After Deleting Duplicate Characters
// https://leetcode.com/problems/lexicographically_smallest_string_after_deleting_duplicate_characters/

class Solution {
    public String lexSmallestAfterDeletion(String s) {
        int[] cnt = new int[26];
        for (char c : s.toCharArray()) cnt[c - 'a']++;
        StringBuilder stk = new StringBuilder();
        for (char c : s.toCharArray()) {
            while (stk.length() > 0 && stk.charAt(stk.length() - 1) > c
                    && cnt[stk.charAt(stk.length() - 1) - 'a'] > 1) {
                cnt[stk.charAt(stk.length() - 1) - 'a']--;
                stk.deleteCharAt(stk.length() - 1);
            }
            stk.append(c);
        }
        while (cnt[stk.charAt(stk.length() - 1) - 'a'] > 1) {
            cnt[stk.charAt(stk.length() - 1) - 'a']--;
            stk.deleteCharAt(stk.length() - 1);
        }
        return stk.toString();
    }
}
