// LeetCode 2379 - Minimum Recolors to Get K Consecutive Black Blocks
// https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution {
    public int minimumRecolors(String blocks, int k) {
        int white = 0;
        for (int i = 0; i < k; i++) if (blocks.charAt(i) == 'W') white++;
        int ans = white;
        for (int i = k; i < blocks.length(); i++) {
            if (blocks.charAt(i) == 'W') white++;
            if (blocks.charAt(i - k) == 'W') white--;
            ans = Math.min(ans, white);
        }
        return ans;
    }
}
