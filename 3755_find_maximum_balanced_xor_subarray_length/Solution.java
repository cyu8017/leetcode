// LeetCode 3755 - Find Maximum Balanced Xor Subarray Length
// https://leetcode.com/problems/find_maximum_balanced_xor_subarray_length/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int maxBalancedSubarray(int[] nums) {
        Map<Long, Integer> d = new HashMap<>();
        int a = 0, b = nums.length, ans = 0;
        d.put((long) b, -1);
        for (int i = 0; i < nums.length; i++) {
            a ^= nums[i];
            if (nums[i] % 2 == 0) b++;
            else b--;
            long key = ((long) a << 32) | (b & 0xffffffffL);
            if (d.containsKey(key)) ans = Math.max(ans, i - d.get(key));
            else d.put(key, i);
        }
        return ans;
    }
}
