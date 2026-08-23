// LeetCode 0727 - Minimum Window Subsequence
// https://leetcode.com/problems/minimum-window-subsequence/

public class Solution {
    public string MinWindow(string s1, string s2) {
        int m = s1.Length, n = s2.Length;
        string best = "";
        int i = 0;
        while (i < m) {
            int j = 0, k = i;
            while (k < m && j < n) {
                if (s1[k] == s2[j]) j++;
                k++;
            }
            if (j < n) break;
            int end = k - 1;
            j = n - 1;
            k = end;
            while (j >= 0) {
                if (s1[k] == s2[j]) j--;
                k--;
            }
            int start = k + 1;
            if (best.Length == 0 || end - start + 1 < best.Length) best = s1.Substring(start, end - start + 1);
            i = start + 1;
        }
        return best;
    }
}
