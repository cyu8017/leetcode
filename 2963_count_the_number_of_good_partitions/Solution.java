// LeetCode 2963 - Count the Number of Good Partitions
// https://leetcode.com/problems/count-the-number-of-good-partitions/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int numberOfGoodPartitions(int[] nums) {
        final int mod = 1000000007;
        var last = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) last.put(nums[i], i);
        int ans = 1, end = 0;
        for (int i = 0; i < nums.length; i++) {
            if (last.get(nums[i]) > end) end = last.get(nums[i]);
            if (i == end && i != nums.length - 1) ans = (int)(ans * 2L % mod);
        }
        return ans;
    }
}
