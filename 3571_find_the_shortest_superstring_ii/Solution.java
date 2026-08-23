// LeetCode 3571 - Find the Shortest Superstring II
// https://leetcode.com/problems/find-the-shortest-superstring-ii/

class Solution {
    public String shortestSuperstring(String s1, String s2) {
        if (s1.length() > s2.length()) return shortestSuperstring(s2, s1);
        int m = s1.length();
        if (s2.contains(s1)) return s2;
        for (int i = 0; i < m; i++) {
            if (s2.startsWith(s1.substring(i))) return s1.substring(0, i) + s2;
            int len = m - i;
            if (s2.length() >= len && s2.substring(s2.length() - len) == s1.substring(0, len))
                return s2 + s1.substring(m - i);
        }
        return s1 + s2;
    }
}
