// LeetCode 1467 - Probability Of A Two Boxes Having The Same Number Of Distinct Balls
// https://leetcode.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls/

using System.Linq;
public class Solution {
    long good, total; int half; int[] balls;
    public double GetProbability(int[] balls) {
        this.balls = balls; half = balls.Sum() / 2; good = total = 0;
        Dfs(0, 0, 0, 1); return (double)good / total;
    }
    void Dfs(int i, int left, int dl, long ways) {
        if (i == balls.Length) {
            if (left == half) { total += ways; if (dl == 0) good += ways; }
            return;
        }
        for (int x = 0; x <= balls[i]; x++)
            if (left + x <= half)
                Dfs(i + 1, left + x, dl + (x > 0 ? 1 : 0) - (x < balls[i] ? 1 : 0),
                    ways * Comb(balls[i], x));
    }
    long Comb(int n, int k) {
        if (k < 0 || k > n) return 0;
        long r = 1;
        for (int i = 1; i <= k; i++) r = r * (n - k + i) / i;
        return r;
    }
}
