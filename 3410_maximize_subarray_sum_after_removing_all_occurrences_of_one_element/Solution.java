// LeetCode 3410 - Maximize Subarray Sum After Removing All Occurrences of One Element
// https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    private long kadane(List<Integer> a) {
        long best = -(1L << 62), cur = 0;
        for (int x : a) {
            cur += x;
            if (cur > best) best = cur;
            if (cur < 0) cur = 0;
        }
        boolean allNeg = true;
        long mx = a.get(0);
        for (int x : a) {
            if (x > mx) mx = x;
            if (x >= 0) allNeg = false;
        }
        if (allNeg) return mx;
        return best;
    }

    private long kadane(int[] a) {
        List<Integer> list = new ArrayList<>();
        for (int x : a) list.add(x);
        return kadane(list);
    }

    public long maxSubarraySum(int[] nums) {
        long ans = kadane(nums);
        Set<Integer> uniq = new HashSet<>();
        for (int x : nums) if (x < 0) uniq.add(x);
        for (int v : uniq) {
            List<Integer> b = new ArrayList<>();
            for (int x : nums) if (x != v) b.add(x);
            if (b.isEmpty()) continue;
            long cand = kadane(b);
            if (cand > ans) ans = cand;
        }
        return ans;
    }
}
