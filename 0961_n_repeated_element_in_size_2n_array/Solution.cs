// LeetCode 0961 - N-Repeated Element in Size 2N Array
// https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

using System.Collections.Generic;

public class Solution {
    public int RepeatedNTimes(int[] nums) {
        var seen = new HashSet<int>();
        foreach (int x in nums) {
            if (seen.Contains(x)) return x;
            seen.Add(x);
        }
        return -1;
    }
}
