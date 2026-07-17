// LeetCode 1762 - Buildings With an Ocean View
// https://leetcode.com/problems/buildings-with-an-ocean-view/

class Solution {
    public int[] findBuildings(int[] heights) {
        int n = heights.length;
        int[] buffer = new int[n];
        int count = 0;
        int tallest = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (heights[i] > tallest) {
                buffer[count++] = i;
                tallest = heights[i];
            }
        }
        int[] ans = new int[count];
        for (int i = 0; i < count; i++) {
            ans[i] = buffer[count - 1 - i];
        }
        return ans;
    }
}
