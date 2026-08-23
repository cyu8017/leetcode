// LeetCode 3640 - Trionic Array II
// https://leetcode.com/problems/trionic-array-ii/

using System;

public class Solution {
    public long MaxSumTrionic(int[] nums) {
        int n = nums.Length, i = 0;
        long ans = long.MinValue;
        while (i < n) {
            int l = i;
            for (i++; i < n && nums[i - 1] < nums[i];) i++;
            if (i == l + 1) continue;
            int p = i - 1;
            long s = (long)nums[p - 1] + nums[p];
            while (i < n && nums[i - 1] > nums[i]) {
                s += nums[i];
                i++;
            }
            if (i == p + 1 || i == n || nums[i - 1] == nums[i]) continue;
            int q = i - 1;
            s += nums[i];
            i++;
            long mx = 0, t = 0;
            while (i < n && nums[i - 1] < nums[i]) {
                t += nums[i];
                i++;
                mx = Math.Max(mx, t);
            }
            s += mx;
            mx = t = 0;
            for (int j = p - 2; j >= l; j--) {
                t += nums[j];
                mx = Math.Max(mx, t);
            }
            s += mx;
            ans = Math.Max(ans, s);
            i = q;
        }
        return ans;
    }
}
