// LeetCode 3691 - Maximum Total Subarray Value II
// https://leetcode.com/problems/maximum-total-subarray-value-ii/

using System;
using System.Collections.Generic;

public class Solution {
    class SparseTableRMQ {
        int n, maxLog;
        int[][] fMax, fMin;
        int[] lg;

        public SparseTableRMQ(int[] data) {
            n = data.Length;
            maxLog = 0;
            while ((1 << maxLog) <= n) maxLog++;
            maxLog++;
            fMax = new int[n][];
            fMin = new int[n][];
            for (int i = 0; i < n; i++) {
                fMax[i] = new int[maxLog];
                fMin[i] = new int[maxLog];
            }
            lg = new int[n + 1];
            for (int i = 2; i <= n; i++) lg[i] = lg[i >> 1] + 1;
            for (int i = 0; i < n; i++) {
                fMax[i][0] = data[i];
                fMin[i][0] = data[i];
            }
            for (int j = 1; j < maxLog; j++) {
                for (int i = 0; i <= n - (1 << j); i++) {
                    fMax[i][j] = Math.Max(fMax[i][j - 1], fMax[i + (1 << (j - 1))][j - 1]);
                    fMin[i][j] = Math.Min(fMin[i][j - 1], fMin[i + (1 << (j - 1))][j - 1]);
                }
            }
        }

        public int QueryMax(int l, int r) {
            int k = lg[r - l + 1];
            return Math.Max(fMax[l][k], fMax[r - (1 << k) + 1][k]);
        }

        public int QueryMin(int l, int r) {
            int k = lg[r - l + 1];
            return Math.Min(fMin[l][k], fMin[r - (1 << k) + 1][k]);
        }
    }

    public long MaxTotalValue(int[] nums, int k) {
        int n = nums.Length;
        var st = new SparseTableRMQ(nums);
        var pq = new PriorityQueue<(int l, int r), long>();
        for (int l = 0; l < n; l++) {
            long val = (long)st.QueryMax(l, n - 1) - st.QueryMin(l, n - 1);
            pq.Enqueue((l, n - 1), -val);
        }
        long ans = 0;
        for (int i = 0; i < k; i++) {
            pq.TryDequeue(out var item, out long negVal);
            long val = -negVal;
            int l = item.l, r = item.r;
            ans += val;
            if (r > l) {
                long nextVal = (long)st.QueryMax(l, r - 1) - st.QueryMin(l, r - 1);
                pq.Enqueue((l, r - 1), -nextVal);
            }
        }
        return ans;
    }
}
