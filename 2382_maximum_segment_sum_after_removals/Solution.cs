// LeetCode 2382 - Maximum Segment Sum After Removals
// https://leetcode.com/problems/maximum-segment-sum-after-removals/

using System;

public class Solution {
    public long[] MaximumSegmentSum(int[] nums, int[] removeQueries) {
        int n = nums.Length;
        int[] parent = new int[n];
        long[] sum = new long[n];
        bool[] active = new bool[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        int Find(int x) {
            if (parent[x] != x) parent[x] = Find(parent[x]);
            return parent[x];
        }
        void Unite(int a, int b) {
            int ra = Find(a), rb = Find(b);
            if (ra == rb) return;
            parent[rb] = ra;
            sum[ra] += sum[rb];
        }
        long[] ans = new long[n];
        long best = 0;
        for (int i = n - 1; i >= 0; i--) {
            ans[i] = best;
            int idx = removeQueries[i];
            active[idx] = true;
            sum[idx] = nums[idx];
            if (idx > 0 && active[idx - 1]) Unite(idx, idx - 1);
            if (idx + 1 < n && active[idx + 1]) Unite(idx, idx + 1);
            best = Math.Max(best, sum[Find(idx)]);
        }
        return ans;
    }
}
