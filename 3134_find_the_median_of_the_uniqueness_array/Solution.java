// LeetCode 3134 - Find the Median of the Uniqueness Array
// https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int medianOfUniquenessArray(int[] nums) {
        int n = nums.length;
        long m = (1L + n) * n / 2;
        int lo = 1, hi = n;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (check(nums, n, m, mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    private boolean check(int[] nums, int n, long m, int mx) {
        Map<Integer, Integer> cnt = new HashMap<>();
        int l = 0;
        long k = 0;
        for (int r = 0; r < n; r++) {
            cnt.put(nums[r], cnt.getOrDefault(nums[r], 0) + 1);
            while (cnt.size() > mx) {
                int y = nums[l++];
                int nv = cnt.get(y) - 1;
                if (nv == 0) cnt.remove(y);
                else cnt.put(y, nv);
            }
            k += r - l + 1;
            if (k >= (m + 1) / 2) return true;
        }
        return false;
    }
}
