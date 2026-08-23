// LeetCode 3555 - Smallest Subarray to Sort in Every Sliding Window
// https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] minSubarraySort(int[] nums, int k) {
        final int inf = 1 << 30;
        int n = nums.length;
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i <= n - k; i++) ans.add(f(nums, i, i + k - 1, inf));
        return ans.stream().mapToInt(Integer::intValue).toArray();
    }

    int f(int[] nums, int i, int j, int inf) {
        int mi = inf, mx = -inf, l = -1, r = -1;
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
}
