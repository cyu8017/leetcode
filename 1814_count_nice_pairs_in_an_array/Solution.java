// LeetCode 1814 - Count Nice Pairs in an Array
// https://leetcode.com/problems/count-nice-pairs-in-an-array/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int countNicePairs(int[] nums) {
        final int mod = 1_000_000_007;
        Map<Integer, Integer> freq = new HashMap<>();
        long ans = 0;

        for (int num : nums) {
            int diff = num - rev(num);
            ans = (ans + freq.getOrDefault(diff, 0)) % mod;
            freq.merge(diff, 1, Integer::sum);
        }

        return (int) ans;
    }

    private int rev(int x) {
        return Integer.parseInt(new StringBuilder(Integer.toString(x)).reverse().toString());
    }
}
