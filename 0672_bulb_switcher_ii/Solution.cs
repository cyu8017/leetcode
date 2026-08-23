// LeetCode 0672 - Bulb Switcher II
// https://leetcode.com/problems/bulb-switcher-ii/

public class Solution {
    public int FlipLights(int n, int presses) {
        n = System.Math.Min(n, 3);
        if (presses == 0) return 1;
        int[] onePress = { 2, 3, 4 };
        int[] twoPress = { 2, 4, 7 };
        int[] manyPress = { 2, 4, 8 };
        if (presses == 1) return onePress[n - 1];
        if (presses == 2) return twoPress[n - 1];
        return manyPress[n - 1];
    }
}
