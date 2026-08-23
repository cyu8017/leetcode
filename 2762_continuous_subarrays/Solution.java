// LeetCode 2762 - Continuous Subarrays
// https://leetcode.com/problems/continuous-subarrays/

import java.util.TreeMap;

class Solution {
    public long continuousSubarrays(int[] nums) {
        long ans = 0;
        int left = 0;
        TreeMap<Integer, Integer> freq = new TreeMap<>();
        for (int right = 0; right < nums.length; right++) {
            freq.put(nums[right], freq.getOrDefault(nums[right], 0) + 1);
            while (freq.lastKey() - freq.firstKey() > 2) {
                int v = nums[left++];
                int c = freq.get(v) - 1;
                if (c == 0) freq.remove(v);
                else freq.put(v, c);
            }
            ans += right - left + 1;
        }
        return ans;
    }
}
