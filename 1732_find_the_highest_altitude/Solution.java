// LeetCode 1732 - Find the Highest Altitude
// https://leetcode.com/problems/find-the-highest-altitude/

class Solution {
    public int largestAltitude(int[] gain) {
        int altitude = 0;
        int best = 0;
        for (int change : gain) {
            altitude += change;
            best = Math.max(best, altitude);
        }
        return best;
    }
}
