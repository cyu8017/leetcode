// LeetCode 1402 - Reducing Dishes
// https://leetcode.com/problems/reducing-dishes/

using System;
public class Solution {
    public int MaxSatisfaction(int[] satisfaction) {
        Array.Sort(satisfaction); Array.Reverse(satisfaction);
        int total = 0, answer = 0;
        foreach (int value in satisfaction) {
            if (total + value <= 0) break;
            total += value; answer += total;
        }
        return answer;
    }
}
