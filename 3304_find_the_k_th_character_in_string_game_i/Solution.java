// LeetCode 3304 - Find the K-th Character in String Game I
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

class Solution {
    public char kthCharacter(int k) {
        StringBuilder s = new StringBuilder("a");
        while (s.length() < k) {
            int n = s.length();
            for (int i = 0; i < n; i++) s.append((char) ('a' + ((s.charAt(i) - 'a' + 1) % 26)));
        }
        return s.charAt(k - 1);
    }
}
