// LeetCode 3410 - Maximize Subarray Sum After Removing All Occurrences of One Element
// https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/

using System.Collections.Generic;

public class Solution {
    long Kadane(IList<int> a) {
        long best = -(1L << 62), cur = 0;
        foreach (int x in a) {
            cur += x;
            if (cur > best) best = cur;
            if (cur < 0) cur = 0;
        }
        bool allNeg = true;
        long mx = a[0];
        foreach (int x in a) {
            if (x > mx) mx = x;
            if (x >= 0) allNeg = false;
        }
        if (allNeg) return mx;
        return best;
    }

    public long MaxSubarraySum(int[] nums) {
        long ans = Kadane(nums);
        var uniq = new HashSet<int>();
        foreach (int x in nums) if (x < 0) uniq.Add(x);
        foreach (int v in uniq) {
            var b = new List<int>();
            foreach (int x in nums) if (x != v) b.Add(x);
            if (b.Count == 0) continue;
            long cand = Kadane(b);
            if (cand > ans) ans = cand;
        }
        return ans;
    }
}
