// LeetCode 3434 - Maximum Frequency After Subarray Operation
// https://leetcode.com/problems/maximum-frequency-after-subarray-operation/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int maxFrequency(int[] nums, int k) {
        int base = 0;
        for (int x : nums) if (x == k) base++;
        int ans = base;
        Set<Integer> uniq = new HashSet<>();
        for (int x : nums) uniq.add(x);
        for (int v : uniq) {
            if (v == k) continue;
            int best = 0, cur = 0;
            for (int x : nums) {
                int delta = 0;
                if (x == v) delta = 1;
                else if (x == k) delta = -1;
                cur += delta;
                if (cur < 0) cur = 0;
                if (cur > best) best = cur;
            }
            if (base + best > ans) ans = base + best;
        }
        return ans;
    }
}
