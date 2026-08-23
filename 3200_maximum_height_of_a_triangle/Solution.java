// LeetCode 3200 - Maximum Height of a Triangle
// https://leetcode.com/problems/maximum-height-of-a-triangle/

class Solution {
    public int maxHeightOfTriangle(int red, int blue) {
        int ans = 0;
        for (int k = 0; k < 2; k++) {
            int[] c = { red, blue };
            for (int i = 1, j = k; i <= c[j]; i++, j ^= 1) {
                c[j] -= i;
                ans = Math.max(ans, i);
            }
        }
        return ans;
    }
}
