// LeetCode 3984 - Divisible Game
// https://leetcode.com/problems/divisible-game/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int divisibleGame(int[] nums) {
        Set<Integer> candidates = new HashSet<>();
        candidates.add(2);
        for (int value : nums) {
            for (int divisor = 2; divisor * divisor <= value; divisor++) {
                if (value % divisor != 0) continue;
                candidates.add(divisor);
                candidates.add(value / divisor);
            }
            if (value > 1) candidates.add(value);
        }
        long bestScore = -(1L << 62);
        int bestK = 0;
        for (int k : candidates) {
            long ending = 0, score = 0;
            for (int i = 0; i < nums.length; i++) {
                int value = nums[i];
                long contribution = -((long) value);
                if (value % k == 0) contribution = value;
                if (i == 0 || ending + contribution < contribution) ending = contribution;
                else ending += contribution;
                if (i == 0 || ending > score) score = ending;
            }
            if (score > bestScore || (score == bestScore && k < bestK)) {
                bestScore = score;
                bestK = k;
            }
        }
        final long mod = 1000000007L;
        long answer = (bestScore % mod) * bestK % mod;
        if (answer < 0) answer += mod;
        return (int) answer;
    }
}
