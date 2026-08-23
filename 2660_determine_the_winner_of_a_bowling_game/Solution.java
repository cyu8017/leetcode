// LeetCode 2660 - Determine the Winner of a Bowling Game
// https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/

class Solution {
    public int isWinner(int[] player1, int[] player2) {
        int a = score(player1), b = score(player2);
        if (a > b) return 1;
        if (b > a) return 2;
        return 0;
    }

    private int score(int[] p) {
        int s = 0;
        for (int i = 0; i < p.length; i++) {
            int mul = 1;
            if ((i > 0 && p[i - 1] == 10) || (i > 1 && p[i - 2] == 10)) mul = 2;
            s += mul * p[i];
        }
        return s;
    }
}
