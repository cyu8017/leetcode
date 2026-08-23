// LeetCode 3487 - Maximum Unique Subarray Sum After Deletion
// https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int maxSum(int[] nums) {
        Set<Integer> seen = new HashSet<>();
        int sum = 0;
        boolean hasPos = false;
        int maxNeg = (int) (-1e9);
        for (int x : nums) {
            if (x < 0) {
                if (x > maxNeg) maxNeg = x;
                continue;
            }
            hasPos = true;
            if (seen.add(x)) sum += x;
        }
        return hasPos ? sum : maxNeg;
    }
}
