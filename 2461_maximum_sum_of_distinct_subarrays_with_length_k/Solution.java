// LeetCode 2461 - Maximum Sum of Distinct Subarrays With Length K
// https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        Map<Integer, Integer> cnt = new HashMap<>();
        long sum = 0, ans = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
            cnt.put(nums[i], cnt.getOrDefault(nums[i], 0) + 1);
            if (i >= k) {
                int y = nums[i - k];
                sum -= y;
                int c = cnt.get(y) - 1;
                if (c == 0) cnt.remove(y);
                else cnt.put(y, c);
            }
            if (i >= k - 1 && cnt.size() == k && sum > ans) ans = sum;
        }
        return ans;
    }
}
