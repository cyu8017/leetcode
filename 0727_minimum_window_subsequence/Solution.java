// LeetCode 0727 - Minimum Window Subsequence
// https://leetcode.com/problems/minimum-window-subsequence/

class Solution {
    public String minWindow(String s1, String s2) {
        int m = s1.length(), n = s2.length();
        String best = "";
        int i = 0;
        while (i < m) {
            int j = 0, k = i;
            while (k < m && j < n) {
                if (s1.charAt(k) == s2.charAt(j)) j++;
                k++;
            }
            if (j < n) break;
            int end = k - 1;
            j = n - 1;
            k = end;
            while (j >= 0) {
                if (s1.charAt(k) == s2.charAt(j)) j--;
                k--;
            }
            int start = k + 1;
            if (best.isEmpty() || end - start + 1 < best.length()) best = s1.substring(start, end + 1);
            i = start + 1;
        }
        return best;
    }
}
