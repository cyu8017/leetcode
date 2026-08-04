// LeetCode 1921 - Eliminate Maximum Number of Monsters
// https://leetcode.com/problems/eliminate-maximum-number-of-monsters/

import java.util.*;

class Solution {
    public int eliminateMaximum(int[] dist, int[] speed) {
        int n = dist.length;
        int[] arrival = new int[n];
        for (int i = 0; i < n; i++) arrival[i] = (dist[i] + speed[i] - 1) / speed[i];
        Arrays.sort(arrival);
        for (int i = 0; i < n; i++) {
            if (arrival[i] <= i) return i;
        }
        return n;
    }
}
