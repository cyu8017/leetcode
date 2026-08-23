// LeetCode 2829 - Determine the Minimum Sum of a k-avoiding Array
// https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int minimumSum(int n, int k) {
        var used = new HashSet<Integer>();
        int sum = 0, x = 1;
        while (used.size() < n) {
            if (!used.contains(k - x)) {
                used.add(x);
                sum += x;
            }
            x++;
        }
        return sum;
    }
}
