// LeetCode 3487 - Maximum Unique Subarray Sum After Deletion
// https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/

using System.Collections.Generic;

public class Solution {
    public int MaxSum(int[] nums) {
        var seen = new HashSet<int>();
        int sum = 0;
        bool hasPos = false;
        int maxNeg = (int)(-1e9);
        foreach (int x in nums) {
            if (x < 0) {
                if (x > maxNeg) maxNeg = x;
                continue;
            }
            hasPos = true;
            if (seen.Add(x)) sum += x;
        }
        return hasPos ? sum : maxNeg;
    }
}
