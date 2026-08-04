// LeetCode 1163 - Last Substring in Lexicographical Order
// https://leetcode.com/problems/last-substring-in-lexicographical-order/

class Solution {
    public String lastSubstring(String s) {
        int i = 0, j = 1, k = 0, n = s.length();
        while (j + k < n) {
            if (s.charAt(i + k) == s.charAt(j + k)) { k++; continue; }
            if (s.charAt(i + k) > s.charAt(j + k)) j = j + k + 1;
            else { i = Math.max(i + k + 1, j); j = i + 1; }
            k = 0;
        }
        return s.substring(i);
    }
}
