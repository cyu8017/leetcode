// LeetCode 1590 - Make Sum Divisible by P
// https://leetcode.com/problems/make-sum-divisible-by-p/

import java.util.*;

class Solution {
    public int minSubarray(int[] nums, int p) {
        int total = 0;
        for (int x : nums) {
            total = (total + x) % p;
        }
        if (total == 0) {
            return 0;
        }
        int target = total;
        Map<Integer, Integer> seen = new HashMap<>();
        seen.put(0, -1);
        int prefix = 0;
        int answer = nums.length;
        for (int i = 0; i < nums.length; i++) {
            prefix = (prefix + nums[i]) % p;
            int need = (prefix - target + p) % p;
            if (seen.containsKey(need)) {
                answer = Math.min(answer, i - seen.get(need));
            }
            seen.put(prefix, i);
        }
        return answer < nums.length ? answer : -1;
    }
}
