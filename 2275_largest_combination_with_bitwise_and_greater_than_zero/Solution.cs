// LeetCode 2275 - Largest Combination With Bitwise AND Greater Than Zero
// https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/

using System;

public class Solution {
    public int LargestCombination(int[] candidates) {
        int ans = 0;
        for (int bit = 0; bit < 24; bit++) {
            int cnt = 0;
            foreach (int x in candidates) if (((x >> bit) & 1) != 0) cnt++;
            ans = Math.Max(ans, cnt);
        }
        return ans;
    }
}
