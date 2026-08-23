// LeetCode 2904 - Shortest and Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

class Solution {
    public String shortestBeautifulSubstring(String s, int k) {
        String ans = "";
        int n = s.length();
        for (int i = 0; i < n; i++) {
            int ones = 0;
            for (int j = i; j < n; j++) {
                if (s.charAt(j) == '1') ones++;
                if (ones == k) {
                    String cand = s.substring(i, j + 1);
                    if (ans.isEmpty() || cand.length() < ans.length()
                            || (cand.length() == ans.length() && cand.compareTo(ans) < 0))
                        ans = cand;
                    break;
                }
                if (ones > k) break;
            }
        }
        return ans;
    }
}
