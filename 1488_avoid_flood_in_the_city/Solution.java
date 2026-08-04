// LeetCode 1488 - Avoid Flood In The City
// https://leetcode.com/problems/avoid-flood-in-the-city/

import java.util.*;

class Solution {
    public int[] avoidFlood(int[] rains) {
        var ans = new int[rains.length];
        for (int i = 0; i < ans.length; i++) ans[i] = -1;
        var full = new HashMap<>();
        var dry = new ArrayList<>();
        for (int i = 0; i < rains.length; i++) {
            int lake = rains[i];
            if (lake == 0) { dry.add(i); ans[i] = 1; }
            else {
                if (full.containsKey(lake)) {
                    int j = dry.BinarySearch(full[lake]);
                    if (j < 0) j = ~j;
                    if (j == dry.size()) return Arrays.Empty<int>();
                    ans[dry[j]] = lake; dry.remove(j);
                }
                full[lake] = i;
            }
        }
        return ans;
    }
}
