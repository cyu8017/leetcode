// LeetCode 3583 - Count Special Triplets
// https://leetcode.com/problems/count-special-triplets/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int specialTriplets(int[] nums) {
        var left = new HashMap<Integer, Integer>();
        var right = new HashMap<Integer, Integer>();
        for (int x : nums) {
            if (!right.containsKey(x)) right.put(x, 0);
            right.put(x, right.get(x) + 1);
        }
        long ans = 0, mod = 1000000007;
        for (int x : nums) {
            right.put(x, right.get(x) - 1);
            long lv = left.containsKey(x * 2) ? left.get(x * 2) : 0;
            long rv = right.containsKey(x * 2) ? right.get(x * 2) : 0;
            ans = (ans + lv * rv % mod) % mod;
            if (!left.containsKey(x)) left.put(x, 0);
            left.put(x, left.get(x) + 1);
        }
        return (int)ans;
    }
}
