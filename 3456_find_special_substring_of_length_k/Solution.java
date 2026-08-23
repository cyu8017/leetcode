// LeetCode 3456 - Find Special Substring of Length K
// https://leetcode.com/problems/find-special-substring-of-length-k/

class Solution {
    public boolean hasSpecialSubstring(String s, int k) {
        int n = s.length();
        for (int i = 0; i + k <= n; i++) {
            boolean ok = true;
            for (int j = i + 1; j < i + k; j++) {
                if (s.charAt(j) != s.charAt(i)) { ok = false; break; }
            }
            if (!ok) continue;
            if (i > 0 && s.charAt(i - 1) == s.charAt(i)) continue;
            if (i + k < n && s.charAt(i + k) == s.charAt(i)) continue;
            return true;
        }
        return false;
    }
}
