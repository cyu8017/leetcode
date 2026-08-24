// LeetCode 2261 - K Divisible Elements Subarrays
// https://leetcode.com/problems/k-divisible-elements-subarrays/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int countDistinct(int[] nums, int k, int p) {
        int n = nums.length;
        var seen = new HashSet<String>();
        for (int i = 0; i < n; i++) {
            int div = 0;
            var key = new StringBuilder();
            for (int j = i; j < n; j++) {
                if (nums[j] % p == 0) div++;
                if (div > k) break;
                key.append(nums[j] + 1).append(',');
                seen.add(key.toString());
            }
        }
        return seen.size();
    }
}
