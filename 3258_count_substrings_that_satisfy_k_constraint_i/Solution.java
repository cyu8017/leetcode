// LeetCode 3258 - Count Substrings That Satisfy K-Constraint I
// https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/

class Solution {
    public int countKConstraintSubstrings(String s, int k) {
        int ans = 0, n = s.length();
        for (int i = 0; i < n; i++) {
            int z = 0, o = 0;
            for (int j = i; j < n; j++) {
                if (s.charAt(j) == '0') z++; else o++;
                if (z <= k || o <= k) ans++;
                else break;
            }
        }
        return ans;
    }
}
