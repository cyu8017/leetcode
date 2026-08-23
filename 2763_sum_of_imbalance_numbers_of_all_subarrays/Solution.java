// LeetCode 2763 - Sum of Imbalance Numbers of All Subarrays
// https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/

import java.util.HashSet;
import java.util.Set;
import java.util.TreeSet;

class Solution {
    public int sumImbalanceNumbers(int[] nums) {
        int n = nums.length, ans = 0;
        for (int i = 0; i < n; i++) {
            Set<Integer> seen = new HashSet<>();
            TreeSet<Integer> sortedVals = new TreeSet<>();
            int imbalance = 0;
            for (int j = i; j < n; j++) {
                int x = nums[j];
                if (!seen.contains(x)) {
                    seen.add(x);
                    Integer next = sortedVals.ceiling(x);
                    Integer prev = sortedVals.floor(x);
                    if (prev != null && x - prev != 1) imbalance++;
                    if (next != null && next - x != 1) imbalance++;
                    if (prev != null && next != null && next - prev > 1) imbalance--;
                    sortedVals.add(x);
                }
                ans += imbalance;
            }
        }
        return ans;
    }
}
