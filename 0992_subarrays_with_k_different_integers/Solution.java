// LeetCode 0992 - Subarrays with K Different Integers
// https://leetcode.com/problems/subarrays-with-k-different-integers/

import java.util.*;

class Solution {
    public int subarraysWithKDistinct(int[] nums, int k) {
        return atMost(nums, k) - atMost(nums, k - 1);
    }

    private int atMost(int[] nums, int m) {
        if (m < 0) return 0;
        Map<Integer, Integer> count = new HashMap<>();
        int left = 0, ans = 0;
        for (int right = 0; right < nums.length; right++) {
            count.merge(nums[right], 1, Integer::sum);
            while (count.size() > m) {
                int v = nums[left++];
                if (count.merge(v, -1, Integer::sum) == 0) count.remove(v);
            }
            ans += right - left + 1;
        }
        return ans;
    }
}
