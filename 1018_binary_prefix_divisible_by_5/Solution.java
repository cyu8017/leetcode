// LeetCode 1018 - Binary Prefix Divisible By 5
// https://leetcode.com/problems/binary-prefix-divisible-by-5/

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Boolean> prefixesDivBy5(int[] nums) {
        List<Boolean> ans = new ArrayList<>(nums.length);
        int rem = 0;
        for (int bit : nums) {
            rem = (rem * 2 + bit) % 5;
            ans.add(rem == 0);
        }
        return ans;
    }
}
