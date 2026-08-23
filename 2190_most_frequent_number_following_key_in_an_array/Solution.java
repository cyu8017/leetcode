// LeetCode 2190 - Most Frequent Number Following Key In an Array
// https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

import java.util.*;

class Solution {
    public int mostFrequent(int[] nums, int key) {
        Map<Integer, Integer> freq = new HashMap<>();
        int best = 0, ans = 0;
        for (int i = 0; i + 1 < nums.length; i++) {
            if (nums[i] == key) {
                int v = freq.merge(nums[i + 1], 1, Integer::sum);
                if (v > best) { best = v; ans = nums[i + 1]; }
            }
        }
        return ans;
    }
}
