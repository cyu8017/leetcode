// LeetCode 3258 - Count Substrings That Satisfy K-Constraint I
// https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/

public class Solution {
    public int CountKConstraintSubstrings(string s, int k) {
        int ans = 0, n = s.Length;
        for (int i = 0; i < n; i++) {
            int z = 0, o = 0;
            for (int j = i; j < n; j++) {
                if (s[j] == '0') z++; else o++;
                if (z <= k || o <= k) ans++;
                else break;
            }
        }
        return ans;
    }
}
