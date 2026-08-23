// LeetCode 3347 - Maximum Frequency of an Element After Performing Operations II
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Solution {
    public int maxFrequency(int[] nums, int k, int numOperations) {
        Arrays.sort(nums);
        Map<Integer, Integer> freq = new HashMap<>();
        for (int x : nums) freq.merge(x, 1, Integer::sum);
        int ans = 1;
        List<Integer> candidates = new ArrayList<>();
        Set<Integer> seen = new HashSet<>();
        for (int x : nums) {
            for (int t : new int[] {x - k, x, x + k}) {
                if (seen.add(t)) candidates.add(t);
            }
        }
        for (int t : candidates) {
            int lo = lowerBound(nums, t - k);
            int hi = upperBound(nums, t + k);
            int can = hi - lo;
            int f = freq.getOrDefault(t, 0);
            int use = Math.min(can, f + numOperations);
            ans = Math.max(ans, use);
        }
        return ans;
    }

    private static int lowerBound(int[] a, int x) {
        int lo = 0, hi = a.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    private static int upperBound(int[] a, int x) {
        int lo = 0, hi = a.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
