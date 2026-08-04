// LeetCode 1550 - Three Consecutive Odds
// https://leetcode.com/problems/three-consecutive-odds/

class Solution {
    public boolean threeConsecutiveOdds(int[] arr) {
        int run = 0;
        for (int value : arr) {
            if ((value & 1) == 1) {
                run++;
                if (run == 3) {
                    return true;
                }
            } else {
                run = 0;
            }
        }
        return false;
    }
}
