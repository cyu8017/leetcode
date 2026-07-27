// LeetCode 1655 - Distribute Repeating Integers
// https://leetcode.com/problems/distribute-repeating-integers/

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

class Solution {
    public boolean canDistribute(int[] nums, int[] quantity) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int num : nums) {
            freq.merge(num, 1, Integer::sum);
        }
        List<Integer> counts = new ArrayList<>(freq.values());
        Arrays.sort(quantity);
        for (int i = 0, j = quantity.length - 1; i < j; i++, j--) {
            int tmp = quantity[i];
            quantity[i] = quantity[j];
            quantity[j] = tmp;
        }
        int m = quantity.length;
        int[] sums = new int[1 << m];
        for (int mask = 1; mask < (1 << m); mask++) {
            int bit = mask & -mask;
            sums[mask] = sums[mask ^ bit] + quantity[Integer.numberOfTrailingZeros(bit)];
        }
        Set<Integer> dp = new HashSet<>();
        dp.add(0);
        for (int c : counts) {
            Set<Integer> next = new HashSet<>(dp);
            for (int mask : dp) {
                int left = ((1 << m) - 1) ^ mask;
                int sub = left;
                while (sub > 0) {
                    if (sums[sub] <= c) {
                        next.add(mask | sub);
                    }
                    sub = (sub - 1) & left;
                }
            }
            dp = next;
        }
        return dp.contains((1 << m) - 1);
    }
}
