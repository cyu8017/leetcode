// LeetCode 0755 - Pour Water
// https://leetcode.com/problems/pour-water/

class Solution {
    public int[] pourWater(int[] heights, int volume, int k) {
        for (int v = 0; v < volume; v++) {
            int index = k;
            for (int i = k - 1; i >= 0; i--) {
                if (heights[i] > heights[index]) break;
                if (heights[i] < heights[index]) index = i;
            }
            if (index != k) { heights[index]++; continue; }
            index = k;
            for (int i = k + 1; i < heights.length; i++) {
                if (heights[i] > heights[index]) break;
                if (heights[i] < heights[index]) index = i;
            }
            heights[index]++;
        }
        return heights;
    }
}
