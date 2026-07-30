// LeetCode 1550 - Three Consecutive Odds
// https://leetcode.com/problems/three-consecutive-odds/

public class Solution {
    public bool ThreeConsecutiveOdds(int[] arr) {
        int run = 0;
        foreach (int value in arr) {
            run = (value & 1) == 1 ? run + 1 : 0;
            if (run == 3) return true;
        }
        return false;
    }
}
