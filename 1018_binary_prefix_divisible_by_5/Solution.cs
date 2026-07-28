// LeetCode 1018 - Binary Prefix Divisible By 5
// https://leetcode.com/problems/binary-prefix-divisible-by-5/

using System.Collections.Generic;

public class Solution {
    public IList<bool> PrefixesDivBy5(int[] nums) {
        var ans = new List<bool>();
        int rem = 0;
        foreach (int bit in nums) {
            rem = (rem * 2 + bit) % 5;
            ans.Add(rem == 0);
        }
        return ans;
    }
}
