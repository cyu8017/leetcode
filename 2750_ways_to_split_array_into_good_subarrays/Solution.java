// LeetCode 2750 - Ways to Split Array Into Good Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-good-subarrays/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int numberOfGoodSubarraySplits(int[] nums) {
        final int MOD = 1_000_000_007;
        List<Integer> ones = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) if (nums[i] == 1) ones.add(i);
        if (ones.isEmpty()) return 0;
        long ans = 1;
        for (int i = 1; i < ones.size(); i++)
            ans = ans * (ones.get(i) - ones.get(i - 1)) % MOD;
        return (int) ans;
    }
}
