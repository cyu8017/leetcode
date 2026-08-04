// LeetCode 1326 - Minimum Number Of Taps To Open To Water A Garden
// https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

class Solution {
    public int minTaps(int n, int[] ranges) {
        var farthest = new int[n + 1];
        for (int center = 0; center < ranges.length; center++) {
            int left = Math.max(0, center - ranges[center]);
            int right = Math.min(n, center + ranges[center]);
            farthest[left] = Math.max(farthest[left], right);
        }
        int taps = 0, end = 0, reach = 0;
        for (int position = 0; position < n; position++) {
            reach = Math.max(reach, farthest[position]);
            if (position == end) {
                if (reach <= position) return -1;
                taps++;
                end = reach;
            }
        }
        return taps;
    }
}
