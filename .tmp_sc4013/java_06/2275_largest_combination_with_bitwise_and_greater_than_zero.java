// LeetCode 2275 - Largest Combination With Bitwise AND Greater Than Zero
// https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

class Solution {
    public int largestCombination(int[] candidates) {
        int ans = 0;
        for (int bit = 0; bit < 24; bit++) {
            int cnt = 0;
            for (int x : candidates) if (((x >> bit) & 1) != 0) cnt++;
            ans = Math.max(ans, cnt);
        }
        return ans;
    }
}
