// LeetCode 2382 - Maximum Segment Sum After Removals
// https://leetcode.com/problems/maximum-segment-sum-after-removals/

class Solution {
    private int[] parent;
    private long[] sum;
    private boolean[] active;

    public long[] maximumSegmentSum(int[] nums, int[] removeQueries) {
        int n = nums.length;
        parent = new int[n];
        sum = new long[n];
        active = new boolean[n];
        for (int i = 0; i < n; i++) parent[i] = i;
        long[] ans = new long[n];
        long best = 0;
        for (int i = n - 1; i >= 0; i--) {
            ans[i] = best;
            int idx = removeQueries[i];
            active[idx] = true;
            sum[idx] = nums[idx];
            if (idx > 0 && active[idx - 1]) unite(idx, idx - 1);
            if (idx + 1 < n && active[idx + 1]) unite(idx, idx + 1);
            best = Math.max(best, sum[find(idx)]);
        }
        return ans;
    }

    private int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    private void unite(int a, int b) {
        int ra = find(a), rb = find(b);
        if (ra == rb) return;
        parent[rb] = ra;
        sum[ra] += sum[rb];
    }
}
