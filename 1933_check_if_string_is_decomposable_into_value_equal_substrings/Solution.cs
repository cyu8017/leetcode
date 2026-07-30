// LeetCode 1933 - Check if String Is Decomposable Into Value-Equal Substrings
// https://leetcode.com/problems/check-if-string-is-decomposable-into-value-equal-substrings/

public class Solution {
    public bool IsDecomposable(string s) {
        int n = s.Length, i = 0, twos = 0;
        while (i < n) {
            int j = i;
            while (j < n && s[j] == s[i]) j++;
            int length = j - i;
            if (length % 3 == 1) return false;
            if (length % 3 == 2) {
                twos++;
                if (twos > 1) return false;
            }
            i = j;
        }
        return twos == 1;
    }
}