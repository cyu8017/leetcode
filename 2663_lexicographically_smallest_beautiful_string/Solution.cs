// LeetCode 2663 - Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/lexicographically-smallest-beautiful-string/

public class Solution {
    public string SmallestBeautifulString(string s, int k) {
        int n = s.Length;
        char[] b = s.ToCharArray();
        for (int i = n - 1; i >= 0; i--) {
            for (char c = (char)(b[i] + 1); c < 'a' + k; c++) {
                if ((i > 0 && c == b[i - 1]) || (i > 1 && c == b[i - 2])) continue;
                b[i] = c;
                for (int j = i + 1; j < n; j++) {
                    for (char nc = 'a'; nc < 'a' + k; nc++) {
                        if ((j > 0 && nc == b[j - 1]) || (j > 1 && nc == b[j - 2])) continue;
                        b[j] = nc;
                        break;
                    }
                }
                return new string(b);
            }
        }
        return "";
    }
}
