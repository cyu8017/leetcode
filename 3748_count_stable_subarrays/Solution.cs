// LeetCode 3748 - Count Stable Subarrays
// https://leetcode.com/problems/count-stable-subarrays/

using System.Collections.Generic;

public class Solution {
    public long[] CountStableSubarrays(int[] nums, int[][] queries) {
        int n = nums.Length;
        var seg = new List<int>();
        var s = new List<long> { 0 };
        int l = 0;
        for (int r = 0; r < n; r++) {
            if (r == n - 1 || nums[r] > nums[r + 1]) {
                seg.Add(l);
                long k = r - l + 1;
                s.Add(s[s.Count - 1] + k * (k + 1) / 2);
                l = r + 1;
            }
        }
        long[] ans = new long[queries.Length];
        for (int idx = 0; idx < queries.Length; idx++) {
            int left = queries[idx][0], right = queries[idx][1];
            int i = LowerBound(seg, left + 1);
            int j = LowerBound(seg, right + 1) - 1;
            if (i > j) {
                long k = right - left + 1;
                ans[idx] = k * (k + 1) / 2;
            } else {
                long a = seg[i] - left;
                long b = right - seg[j] + 1;
                ans[idx] = a * (a + 1) / 2 + s[j] - s[i] + b * (b + 1) / 2;
            }
        }
        return ans;
    }

    static int LowerBound(List<int> a, int x) {
        int lo = 0, hi = a.Count;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (a[mid] < x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }
}
