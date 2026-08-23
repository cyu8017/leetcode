// LeetCode 3474 - Lexicographically Smallest Generated String
// https://leetcode.com/problems/lexicographically-smallest-generated-string/

public class Solution {
    public string GenerateString(string str1, string str2) {
        int n = str1.Length, m = str2.Length;
        int L = n + m - 1;
        char[] ans = new char[L];
        for (int i = 0; i < L; i++) ans[i] = '?';
        for (int i = 0; i < n; i++) {
            if (str1[i] == 'T') {
                for (int j = 0; j < m; j++) {
                    if (ans[i + j] != '?' && ans[i + j] != str2[j]) return "";
                    ans[i + j] = str2[j];
                }
            }
        }
        for (int i = 0; i < L; i++) if (ans[i] == '?') ans[i] = 'a';
        for (int i = 0; i < n; i++) {
            if (str1[i] == 'F') {
                bool match = true;
                for (int j = 0; j < m; j++) if (ans[i + j] != str2[j]) { match = false; break; }
                if (match) {
                    bool changed = false;
                    for (int j = m - 1; j >= 0; j--) {
                        int pos = i + j;
                        bool forced = false;
                        for (int t = 0; t < n; t++) {
                            if (str1[t] == 'T' && pos >= t && pos < t + m) { forced = true; break; }
                        }
                        if (!forced) {
                            ans[pos] = 'b';
                            changed = true;
                            break;
                        }
                    }
                    if (!changed) return "";
                }
            }
        }
        for (int i = 0; i < n; i++) {
            bool match = true;
            for (int j = 0; j < m; j++) if (ans[i + j] != str2[j]) { match = false; break; }
            if (str1[i] == 'T' && !match) return "";
            if (str1[i] == 'F' && match) return "";
        }
        return new string(ans);
    }
}
