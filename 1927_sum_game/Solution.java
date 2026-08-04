// LeetCode 1927 - Sum Game
// https://leetcode.com/problems/sum-game/

class Solution {
    public boolean sumGame(String num) {
        int n = num.length(), half = n / 2;
        return score(num.substring(0, half)) != score(num.substring(half));
    }

    private int score(String s) {
        int q = 0, dig = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '?') q++;
            else dig += c - '0';
        }
        return dig * 2 + q * 9;
    }
}
