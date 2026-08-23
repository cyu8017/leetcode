// LeetCode 2841 - Maximum Sum of Almost Unique Subarray
// https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/

import java.util.HashMap;
import java.util.List;
import java.util.Map;

class Solution {
    public long maxSum(List<Integer> nums, int m, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        long sum = 0, ans = 0;
        for (int i = 0; i < nums.size(); i++) {
            freq.merge(nums.get(i), 1, Integer::sum);
            sum += nums.get(i);
            if (i >= k) {
                int out = nums.get(i - k);
                sum -= out;
                int c = freq.merge(out, -1, Integer::sum);
                if (c == 0) freq.remove(out);
            }
            if (i >= k - 1 && freq.size() >= m) ans = Math.max(ans, sum);
        }
        return ans;
    }
}
