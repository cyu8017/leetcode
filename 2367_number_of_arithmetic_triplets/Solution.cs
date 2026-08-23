// LeetCode 2367 - Number of Arithmetic Triplets
// https://leetcode.com/problems/number-of-arithmetic-triplets/

using System.Collections.Generic;

public class Solution {
    public int ArithmeticTriplets(int[] nums, int diff) {
        var seen = new HashSet<int>(nums);
        int ans = 0;
        foreach (int x in nums)
            if (seen.Contains(x + diff) && seen.Contains(x + 2 * diff)) ans++;
        return ans;
    }
}
