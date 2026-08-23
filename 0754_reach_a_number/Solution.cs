// LeetCode 0754 - Reach a Number
// https://leetcode.com/problems/reach-a-number/

using System;

public class Solution {
    public int ReachNumber(int target) {
        target = Math.Abs(target);
        int steps = 0, total = 0;
        while (total < target || (total - target) % 2 != 0) {
            steps++;
            total += steps;
        }
        return steps;
    }
}
