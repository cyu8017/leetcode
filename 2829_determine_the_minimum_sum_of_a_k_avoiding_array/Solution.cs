// LeetCode 2829 - Determine the Minimum Sum of a k-avoiding Array
// https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/

using System.Collections.Generic;

public class Solution {
    public int MinimumSum(int n, int k) {
        var used = new HashSet<int>();
        int sum = 0, x = 1;
        while (used.Count < n) {
            if (!used.Contains(k - x)) {
                used.Add(x);
                sum += x;
            }
            x++;
        }
        return sum;
    }
}
