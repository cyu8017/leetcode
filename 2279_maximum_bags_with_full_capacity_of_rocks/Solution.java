// LeetCode 2279 - Maximum Bags With Full Capacity of Rocks
// https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

import java.util.Arrays;

class Solution {
    public int maximumBags(int[] capacity, int[] rocks, int additionalRocks) {
        int[] need = new int[capacity.length];
        for (int i = 0; i < capacity.length; i++) need[i] = capacity[i] - rocks[i];
        Arrays.sort(need);
        int ans = 0;
        for (int n : need) {
            if (additionalRocks < n) break;
            additionalRocks -= n;
            ans++;
        }
        return ans;
    }
}
