// LeetCode 2367 - Number of Arithmetic Triplets
// https://leetcode.com/problems/number-of-arithmetic-triplets/

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int arithmeticTriplets(int[] nums, int diff) {
        Set<Integer> seen = new HashSet<>();
        for (int x : nums) seen.add(x);
        int ans = 0;
        for (int x : nums) {
            if (seen.contains(x + diff) && seen.contains(x + 2 * diff)) ans++;
        }
        return ans;
    }
}
