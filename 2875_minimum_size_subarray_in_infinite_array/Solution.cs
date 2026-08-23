// LeetCode 2875 - Minimum Size Subarray in Infinite Array
// https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

using System.Collections.Generic;

public class Solution {
    public int MinSizeSubarray(int[] nums, int target) {
        int n = nums.Length;
        long total = 0;
        foreach (int v in nums) total += v;
        int ans = 1 << 30;
        if (total > 0) {
            int loops = (int)(target / total);
            int remain = (int)(target % total);
            if (remain == 0) return loops * n;
            var arr = new List<int>(nums);
            arr.AddRange(nums);
            int left = 0, sum = 0, best = 1 << 30;
            for (int right = 0; right < arr.Count; right++) {
                sum += arr[right];
                while (sum > remain && left <= right) {
                    sum -= arr[left];
                    left++;
                }
                if (sum == remain && right - left + 1 < best) best = right - left + 1;
            }
            if (best < (1 << 30)) ans = loops * n + best;
        }
        return ans == (1 << 30) ? -1 : ans;
    }
}
