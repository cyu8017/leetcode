// LeetCode 2342 - Max Sum of a Pair With Equal Sum of Digits
// https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int maximumSum(int[] nums) {
        Map<Integer, Integer> best = new HashMap<>();
        int ans = -1;
        for (int x : nums) {
            int ds = digitSum(x);
            if (best.containsKey(ds)) {
                ans = Math.max(ans, best.get(ds) + x);
                if (x > best.get(ds)) best.put(ds, x);
            } else {
                best.put(ds, x);
            }
        }
        return ans;
    }

    private int digitSum(int x) {
        int s = 0;
        while (x > 0) {
            s += x % 10;
            x /= 10;
        }
        return s;
    }
}
