// LeetCode 2537 - Count the Number of Good Subarrays
// https://leetcode.com/problems/count-the-number-of-good-subarrays/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public long countGood(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        long pairs = 0, ans = 0;
        int left = 0;
        for (int right = 0; right < nums.length; right++) {
            pairs += freq.getOrDefault(nums[right], 0);
            freq.put(nums[right], freq.getOrDefault(nums[right], 0) + 1);
            while (pairs >= k) {
                ans += nums.length - right;
                freq.put(nums[left], freq.get(nums[left]) - 1);
                pairs -= freq.get(nums[left]);
                left++;
            }
        }
        return ans;
    }
}
