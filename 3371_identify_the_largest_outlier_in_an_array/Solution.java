// LeetCode 3371 - Identify the Largest Outlier in an Array
// https://leetcode.com/problems/identify-the-largest-outlier-in-an-array/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int getLargestOutlier(int[] nums) {
        int sum = 0;
        Map<Integer, Integer> freq = new HashMap<>();
        for (int x : nums) {
            sum += x;
            freq.merge(x, 1, Integer::sum);
        }
        int ans = Integer.MIN_VALUE;
        for (int x : nums) {
            freq.put(x, freq.get(x) - 1);
            int rem = sum - x;
            if (rem % 2 == 0) {
                int cand = rem / 2;
                if (freq.getOrDefault(cand, 0) > 0 && x > ans) ans = x;
            }
            freq.put(x, freq.get(x) + 1);
        }
        return ans;
    }
}
