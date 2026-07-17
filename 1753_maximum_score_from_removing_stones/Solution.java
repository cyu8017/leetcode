// LeetCode 1753 - Maximum Score From Removing Stones
// https://leetcode.com/problems/maximum-score-from-removing-stones/

import java.util.Arrays;

class Solution {
    public int maximumScore(int a, int b, int c) {
        int[] stones = { a, b, c };
        sortDescending(stones);
        int score = 0;
        while (stones[0] > 0 && stones[1] > 0) {
            stones[0]--;
            stones[1]--;
            score++;
            sortDescending(stones);
        }
        return score;
    }

    private void sortDescending(int[] stones) {
        Arrays.sort(stones);
        int tmp = stones[0];
        stones[0] = stones[2];
        stones[2] = tmp;
    }
}
