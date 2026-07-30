// LeetCode 1578 - Minimum Time to Make Rope Colorful
// https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

using System;

public class Solution {
    public int MinCost(string colors, int[] neededTime) {
        int answer = 0, maximum = 0;
        for (int i = 0; i < neededTime.Length; i++) {
            if (i > 0 && colors[i] != colors[i - 1]) maximum = 0;
            answer += Math.Min(maximum, neededTime[i]);
            maximum = Math.Max(maximum, neededTime[i]);
        }
        return answer;
    }
}
