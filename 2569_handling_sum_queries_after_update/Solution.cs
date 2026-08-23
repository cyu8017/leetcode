// LeetCode 2569 - Handling Sum Queries After Update
// https://leetcode.com/problems/handling-sum-queries-after-update/

using System.Collections.Generic;

public class Solution {
    public long[] HandleQuery(int[] nums1, int[] nums2, int[][] queries) {
        int n = nums1.Length;
        int[] ones = new int[4 * n];
        bool[] lazy = new bool[4 * n];

        void Build(int idx, int l, int r) {
            if (l == r) {
                ones[idx] = nums1[l];
                return;
            }
            int m = (l + r) / 2;
            Build(idx * 2, l, m);
            Build(idx * 2 + 1, m + 1, r);
            ones[idx] = ones[idx * 2] + ones[idx * 2 + 1];
        }

        void Apply(int idx, int l, int r) {
            ones[idx] = (r - l + 1) - ones[idx];
            lazy[idx] = !lazy[idx];
        }

        void Push(int idx, int l, int r) {
            if (lazy[idx] && l != r) {
                int m = (l + r) / 2;
                Apply(idx * 2, l, m);
                Apply(idx * 2 + 1, m + 1, r);
                lazy[idx] = false;
            }
        }

        void Update(int idx, int l, int r, int ql, int qr) {
            if (ql <= l && r <= qr) {
                Apply(idx, l, r);
                return;
            }
            Push(idx, l, r);
            int m = (l + r) / 2;
            if (ql <= m) Update(idx * 2, l, m, ql, qr);
            if (qr > m) Update(idx * 2 + 1, m + 1, r, ql, qr);
            ones[idx] = ones[idx * 2] + ones[idx * 2 + 1];
        }

        Build(1, 0, n - 1);
        long sum2 = 0;
        foreach (int x in nums2) sum2 += x;
        var ans = new List<long>();
        foreach (var q in queries) {
            if (q[0] == 1) Update(1, 0, n - 1, q[1], q[2]);
            else if (q[0] == 2) sum2 += (long)q[1] * ones[1];
            else ans.Add(sum2);
        }
        return ans.ToArray();
    }
}
