// LeetCode 1467 - Probability Of A Two Boxes Having The Same Number Of Distinct Balls
// https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/

class Solution {
    private long good, total;
    private int half;
    private int[] balls;
    private long[][] comb;

    public double getProbability(int[] balls) {
        this.balls = balls;
        int sum = 0;
        for (int b : balls) sum += b;
        half = sum / 2;
        int max = 0;
        for (int b : balls) max = Math.max(max, b);
        comb = new long[max + 1][max + 1];
        for (int i = 0; i <= max; i++) {
            comb[i][0] = comb[i][i] = 1;
            for (int j = 1; j < i; j++) comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j];
        }
        good = total = 0;
        dfs(0, 0, 0, 1);
        return (double) good / total;
    }

    private void dfs(int i, int left, int dl, long ways) {
        if (i == balls.length) {
            if (left == half) {
                total += ways;
                if (dl == 0) good += ways;
            }
            return;
        }
        for (int x = 0; x <= balls[i]; x++) {
            if (left + x <= half) {
                int delta = (x > 0 ? 1 : 0) - (x < balls[i] ? 1 : 0);
                dfs(i + 1, left + x, dl + delta, ways * comb[balls[i]][x]);
            }
        }
    }
}
