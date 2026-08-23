// LeetCode 2644 - Find the Maximum Divisibility Score
// https://leetcode.com/problems/find-the-maximum-divisibility-score/

class Solution {
    public int maxDivScore(int[] nums, int[] divisors) {
        int best = divisors[0], bestScore = -1;
        for (int d : divisors) {
            int score = 0;
            for (int x : nums) if (x % d == 0) score++;
            if (score > bestScore || (score == bestScore && d < best)) {
                bestScore = score;
                best = d;
            }
        }
        return best;
    }
}
