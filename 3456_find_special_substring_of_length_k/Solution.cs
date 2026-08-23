// LeetCode 3456 - Find Special Substring of Length K
// https://leetcode.com/problems/find-special-substring-of-length-k/

public class Solution {
    public bool HasSpecialSubstring(string s, int k) {
        int n = s.Length;
        for (int i = 0; i + k <= n; i++) {
            bool ok = true;
            for (int j = i + 1; j < i + k; j++) {
                if (s[j] != s[i]) { ok = false; break; }
            }
            if (!ok) continue;
            if (i > 0 && s[i - 1] == s[i]) continue;
            if (i + k < n && s[i + k] == s[i]) continue;
            return true;
        }
        return false;
    }
}
