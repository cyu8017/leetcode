// LeetCode 2379 - Minimum Recolors to Get K Consecutive Black Blocks
// https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

using System;

public class Solution {
    public int MinimumRecolors(string blocks, int k) {
        int white = 0;
        for (int i = 0; i < k; i++) if (blocks[i] == 'W') white++;
        int ans = white;
        for (int i = k; i < blocks.Length; i++) {
            if (blocks[i] == 'W') white++;
            if (blocks[i - k] == 'W') white--;
            ans = Math.Min(ans, white);
        }
        return ans;
    }
}
