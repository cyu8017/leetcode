// LeetCode 0523 - Continuous Subarray Sum
// https://leetcode.com/problems/continuous-subarray-sum/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        Map<Integer, Integer> remainders = new HashMap<>();
        remainders.put(0, -1);
        int prefix = 0;
        for (int index = 0; index < nums.length; index++) {
            prefix += nums[index];
            int mod = k != 0 ? prefix % k : prefix;
            if (remainders.containsKey(mod)) {
                if (index - remainders.get(mod) >= 2) {
                    return true;
                }
            } else {
                remainders.put(mod, index);
            }
        }
        return false;
    }
}
