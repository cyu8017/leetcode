// LeetCode 3474 - Lexicographically Smallest Generated String
// https://leetcode.com/problems/lexicographically-smallest-generated-string/

class Solution {
    public String generateString(String str1, String str2) {
        int n = str1.length(), m = str2.length();
        int L = n + m - 1;
        char[] ans = new char[L];
        ArraysFill(ans, '?');
        for (int i = 0; i < n; i++) {
            if (str1.charAt(i) == 'T') {
                for (int j = 0; j < m; j++) {
                    if (ans[i + j] != '?' && ans[i + j] != str2.charAt(j)) return "";
                    ans[i + j] = str2.charAt(j);
                }
            }
        }
        for (int i = 0; i < L; i++) if (ans[i] == '?') ans[i] = 'a';
        for (int i = 0; i < n; i++) {
            if (str1.charAt(i) == 'F') {
                boolean match = true;
                for (int j = 0; j < m; j++) if (ans[i + j] != str2.charAt(j)) { match = false; break; }
                if (match) {
                    boolean changed = false;
                    for (int j = m - 1; j >= 0; j--) {
                        int pos = i + j;
                        boolean forced = false;
                        for (int t = 0; t < n; t++) {
                            if (str1.charAt(t) == 'T' && pos >= t && pos < t + m) { forced = true; break; }
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
            boolean match = true;
            for (int j = 0; j < m; j++) if (ans[i + j] != str2.charAt(j)) { match = false; break; }
            if (str1.charAt(i) == 'T' && !match) return "";
            if (str1.charAt(i) == 'F' && match) return "";
        }
        return new String(ans);
    }

    private void ArraysFill(char[] a, char c) {
        for (int i = 0; i < a.length; i++) a[i] = c;
    }
}
