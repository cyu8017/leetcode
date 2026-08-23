// LeetCode 2214 - Minimum Health to Beat Game
// https://leetcode.com/problems/minimum-health-to-beat-game/

class Solution {
    public long minimumHealth(int[] damage, int armor) {
        long sum = 0;
        int mx = 0;
        for (int d : damage) { sum += d; mx = Math.max(mx, d); }
        return sum - Math.min(armor, mx) + 1;
    }
}
