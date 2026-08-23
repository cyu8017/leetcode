// LeetCode 2790 - Maximum Number of Groups With Increasing Length
// https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int maxIncreasingGroups(List<Integer> usageLimits) {
        int[] arr = new int[usageLimits.size()];
        for (int i = 0; i < usageLimits.size(); i++) arr[i] = usageLimits.get(i);
        Arrays.sort(arr);
        int ans = 0;
        long sum = 0;
        for (int v : arr) {
            sum += v;
            long need = 1L * (ans + 1) * (ans + 2) / 2;
            if (sum >= need) ans++;
        }
        return ans;
    }
}
