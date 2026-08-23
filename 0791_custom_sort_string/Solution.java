// LeetCode 0791 - Custom Sort String
// https://leetcode.com/problems/custom-sort-string/

class Solution {
    public String customSortString(String order, String s) {
        int[] count = new int[26];
        for (char ch : s.toCharArray()) count[ch - 'a']++;
        StringBuilder sb = new StringBuilder();
        for (char ch : order.toCharArray()) {
            while (count[ch - 'a']-- > 0) sb.append(ch);
        }
        for (int i = 0; i < 26; i++) {
            while (count[i]-- > 0) sb.append((char) ('a' + i));
        }
        return sb.toString();
    }
}
