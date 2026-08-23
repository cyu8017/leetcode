// LeetCode 3096 - Minimum Levels to Gain More Points
// https://leetcode.com/problems/minimum-levels-to-gain-more-points/

public class Solution {
    public int MinimumLevels(int[] possible) {
        int s = 0;
        foreach (int x in possible) s += (x == 0 ? -1 : x);
        int t = 0;
        for (int i = 0; i + 1 < possible.Length; i++) {
            int x = possible[i] == 0 ? -1 : possible[i];
            t += x;
            if (t > s - t) return i + 1;
        }
        return -1;
    }
}
