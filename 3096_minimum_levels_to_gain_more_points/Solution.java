// LeetCode 3096 - Minimum Levels to Gain More Points
// https://leetcode.com/problems/minimum-levels-to-gain-more-points/

class Solution {
    public int minimumLevels(int[] possible) {
        int s = 0;
        for (int x : possible) s += (x == 0 ? -1 : x);
        int t = 0;
        for (int i = 0; i + 1 < possible.length; i++) {
            int x = possible[i] == 0 ? -1 : possible[i];
            t += x;
            if (t > s - t) return i + 1;
        }
        return -1;
    }
}
