// LeetCode 1753 - Maximum Score From Removing Stones
// https://leetcode.com/problems/maximum-score-from-removing-stones/

public class Solution {
    public int MaximumScore(int a, int b, int c) {
        int[] stones = { a, b, c };
        SortDescending(stones);
        int score = 0;
        while (stones[0] > 0 && stones[1] > 0) {
            stones[0]--;
            stones[1]--;
            score++;
            SortDescending(stones);
        }
        return score;
    }

    private void SortDescending(int[] stones) {
        Array.Sort(stones);
        Array.Reverse(stones);
    }
}
