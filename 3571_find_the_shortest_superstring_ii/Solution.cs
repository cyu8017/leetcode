// LeetCode 3571 - Find the Shortest Superstring II
// https://leetcode.com/problems/find-the-shortest-superstring-ii/

public class Solution {
    public string ShortestSuperstring(string s1, string s2) {
        if (s1.Length > s2.Length) return ShortestSuperstring(s2, s1);
        int m = s1.Length;
        if (s2.Contains(s1)) return s2;
        for (int i = 0; i < m; i++) {
            if (s2.StartsWith(s1.Substring(i))) return s1.Substring(0, i) + s2;
            int len = m - i;
            if (s2.Length >= len && s2.Substring(s2.Length - len) == s1.Substring(0, len))
                return s2 + s1.Substring(m - i);
        }
        return s1 + s2;
    }
}
