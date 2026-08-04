// LeetCode 1933 - Check if String Is Decomposable Into Value-Equal Substrings
// https://leetcode.com/problems/check-if-string-is-decomposable-into-value-equal-substrings/

class Solution {
    public boolean isDecomposable(String s) {
        int n = s.length(), i = 0, twos = 0;
        while (i < n) {
            int j = i;
            while (j < n && s.charAt(j) == s.charAt(i)) j++;
            int length = j - i;
            if (length % 3 == 1) return false;
            if (length % 3 == 2) {
                if (++twos > 1) return false;
            }
            i = j;
        }
        return twos == 1;
    }
}
