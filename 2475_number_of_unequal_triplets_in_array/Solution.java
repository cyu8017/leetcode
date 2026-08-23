// LeetCode 2475 - Number of Unequal Triplets in Array
// https://leetcode.com/problems/number-of-unequal-triplets-in-array/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int unequalTriplets(int[] nums) {
        Map<Integer, Integer> cnt = new HashMap<>();
        for (int x : nums) cnt.put(x, cnt.getOrDefault(x, 0) + 1);
        int ans = 0, n = nums.length, left = 0;
        for (int c : cnt.values()) {
            int right = n - left - c;
            ans += left * c * right;
            left += c;
        }
        return ans;
    }
}
