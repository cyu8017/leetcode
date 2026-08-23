// LeetCode 1732 - Find the Highest Altitude
// https://leetcode.com/problems/find-the-highest-altitude/

public class Solution {
    public int LargestAltitude(int[] gain) {
        int altitude = 0;
        int best = 0;
        foreach (int change in gain) {
            altitude += change;
            best = System.Math.Max(best, altitude);
        }
        return best;
    }
}
