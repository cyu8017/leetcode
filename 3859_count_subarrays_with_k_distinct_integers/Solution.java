// LeetCode 3859 - Count Subarrays With K Distinct Integers
// https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/

import java.util.HashMap;
import java.util.Map;

class Solution {
    private int[] nums;
    private int k, m;

    public long countSubarrays(int[] nums, int k, int m) {
        this.nums = nums;
        this.k = k;
        this.m = m;
        return f(k) - f(k + 1);
    }

    private long f(int lim) {
        Map<Integer, Integer> cnt = new HashMap<>();
        long ans = 0;
        int l = 0, t = 0;
        for (int x : nums) {
            int c = cnt.getOrDefault(x, 0) + 1;
            cnt.put(x, c);
            if (c == m) t++;
            while (cnt.size() >= lim && t >= k) {
                int y = nums[l++];
                int cy = cnt.get(y) - 1;
                if (cy == m - 1) t--;
                if (cy == 0) cnt.remove(y);
                else cnt.put(y, cy);
            }
            ans += l;
        }
        return ans;
    }
}
