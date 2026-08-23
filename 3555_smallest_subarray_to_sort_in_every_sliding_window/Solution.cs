// LeetCode 3555 - Smallest Subarray to Sort in Every Sliding Window
// https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/

using System.Collections.Generic;

public class Solution {
    public int[] MinSubarraySort(int[] nums, int k) {
        const int Inf = 1 << 30;
        int n = nums.Length;
        int F(int i, int j) {
            int mi = Inf, mx = -Inf, l = -1, r = -1;
            for (int p = i; p <= j; p++) {
                if (nums[p] < mx) r = p;
                else mx = nums[p];
                int q = j - p + i;
                if (nums[q] > mi) l = q;
                else mi = nums[q];
            }
            if (r == -1) return 0;
            return r - l + 1;
        }
        var ans = new List<int>();
        for (int i = 0; i <= n - k; i++) ans.Add(F(i, i + k - 1));
        return ans.ToArray();
    }
}
