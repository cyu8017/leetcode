// LeetCode 3712 - Sum of Elements With Frequency Divisible by K
// https://leetcode.com/problems/sum-of-elements-with-frequency-divisible-by-k/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int sumDivisibleByK(int[] nums, int k) {
        Map<Integer, Integer> cnt = new HashMap<>();
        for (int x : nums) cnt.merge(x, 1, Integer::sum);
        int ans = 0;
        for (Map.Entry<Integer, Integer> e : cnt.entrySet()) {
            if (e.getValue() % k == 0) ans += e.getKey() * e.getValue();
        }
        return ans;
    }
}
