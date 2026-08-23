// LeetCode 3134 - Find the Median of the Uniqueness Array
// https://leetcode.com/problems/find-the-median-of-the-uniqueness-array/

using System.Collections.Generic;

public class Solution {
    public int MedianOfUniquenessArray(int[] nums) {
        int n = nums.Length;
        long m = (1L + n) * n / 2;
        bool Check(int mx) {
            var cnt = new Dictionary<int, int>();
            int l = 0;
            long k = 0;
            for (int r = 0; r < n; r++) {
                if (!cnt.ContainsKey(nums[r])) cnt[nums[r]] = 0;
                cnt[nums[r]]++;
                while (cnt.Count > mx) {
                    int y = nums[l++];
                    if (--cnt[y] == 0) cnt.Remove(y);
                }
                k += r - l + 1;
                if (k >= (m + 1) / 2) return true;
            }
            return false;
        }
        int lo = 1, hi = n;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (Check(mid)) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
