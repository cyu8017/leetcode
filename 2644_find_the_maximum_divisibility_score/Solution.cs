// LeetCode 2644 - Find the Maximum Divisibility Score
// https://leetcode.com/problems/find-the-maximum-divisibility-score/

public class Solution {
    public int MaxDivScore(int[] nums, int[] divisors) {
        int best = divisors[0], bestScore = -1;
        foreach (int d in divisors) {
            int score = 0;
            foreach (int x in nums) if (x % d == 0) score++;
            if (score > bestScore || (score == bestScore && d < best)) {
                bestScore = score; best = d;
            }
        }
        return best;
    }
}
