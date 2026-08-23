// LeetCode 2660 - Determine the Winner of a Bowling Game
// https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/

public class Solution {
    public int IsWinner(int[] player1, int[] player2) {
        int Score(int[] p) {
            int s = 0;
            for (int i = 0; i < p.Length; i++) {
                int mul = 1;
                if ((i > 0 && p[i - 1] == 10) || (i > 1 && p[i - 2] == 10)) mul = 2;
                s += mul * p[i];
            }
            return s;
        }
        int a = Score(player1), b = Score(player2);
        if (a > b) return 1;
        if (b > a) return 2;
        return 0;
    }
}
