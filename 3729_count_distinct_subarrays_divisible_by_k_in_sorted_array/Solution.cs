// LeetCode 3729 - Count Distinct Subarrays Divisible by K in Sorted Array
// https://leetcode.com/problems/count-distinct-subarrays-divisible-by-k-in-sorted-array/

using System.Collections.Generic;

public class Solution {
    public long NumGoodSubarrays(int[] nums, int k) {
        long ans = 0;
        int s = 0;
        var cnt = new Dictionary<int, int> { [0] = 1 };
        foreach (int x in nums) {
            s = (s + x) % k;
            if (cnt.ContainsKey(s)) ans += cnt[s];
            else cnt[s] = 0;
            cnt[s]++;
        }
        int n = nums.Length;
        for (int i = 0; i < n; ) {
            int j = i + 1;
            while (j < n && nums[j] == nums[i]) j++;
            int m = j - i;
            for (int h = 1; h <= m; h++) {
                if (1L * nums[i] * h % k == 0) ans -= (m - h);
            }
            i = j;
        }
        return ans;
    }
}
