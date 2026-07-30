// LeetCode 1326 - Minimum Number Of Taps To Open To Water A Garden
// https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/

public class Solution {
    public int MinTaps(int n, int[] ranges) {
        var farthest = new int[n + 1];
        for (int center = 0; center < ranges.Length; center++) {
            int left = System.Math.Max(0, center - ranges[center]);
            int right = System.Math.Min(n, center + ranges[center]);
            farthest[left] = System.Math.Max(farthest[left], right);
        }
        int taps = 0, end = 0, reach = 0;
        for (int position = 0; position < n; position++) {
            reach = System.Math.Max(reach, farthest[position]);
            if (position == end) {
                if (reach <= position) return -1;
                taps++;
                end = reach;
            }
        }
        return taps;
    }
}
