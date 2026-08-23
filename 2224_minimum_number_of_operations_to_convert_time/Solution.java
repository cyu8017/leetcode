// LeetCode 2224 - Minimum Number of Operations to Convert Time
// https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

class Solution {
    private int toMin(String t) {
        return (t.charAt(0) - '0') * 600 + (t.charAt(1) - '0') * 60
                + (t.charAt(3) - '0') * 10 + (t.charAt(4) - '0');
    }

    public int convertTime(String current, String correct) {
        int diff = toMin(correct) - toMin(current);
        int ans = 0;
        for (int step : new int[] { 60, 15, 5, 1 }) {
            ans += diff / step;
            diff %= step;
        }
        return ans;
    }
}
