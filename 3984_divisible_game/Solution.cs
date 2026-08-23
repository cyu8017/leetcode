// LeetCode 3984 - Divisible Game
// https://leetcode.com/problems/divisible-game/

using System.Collections.Generic;

public class Solution {
    public int DivisibleGame(int[] nums) {
        var candidates = new HashSet<int> { 2 };
        foreach (int value in nums) {
            for (int divisor = 2; divisor * divisor <= value; divisor++) {
                if (value % divisor != 0) continue;
                candidates.Add(divisor);
                candidates.Add(value / divisor);
            }
            if (value > 1) candidates.Add(value);
        }
        long bestScore = -(1L << 62);
        int bestK = 0;
        foreach (int k in candidates) {
            long ending = 0, score = 0;
            for (int i = 0; i < nums.Length; i++) {
                int value = nums[i];
                long contribution = -((long)value);
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
        const long mod = 1000000007L;
        long answer = (bestScore % mod) * bestK % mod;
        if (answer < 0) answer += mod;
        return (int)answer;
    }
}
