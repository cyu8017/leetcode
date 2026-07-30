// LeetCode 1296 - Divide Array in Sets of K Consecutive Numbers
// https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public bool IsPossibleDivide(int[] nums, int k) {
        if (nums.Length % k != 0) return false;
        var counts = new SortedDictionary<int, int>();
        foreach (int x in nums) {
            if (!counts.ContainsKey(x)) counts[x] = 0;
            counts[x]++;
        }
        foreach (int start in counts.Keys.ToList()) {
            int amount = counts[start];
            if (amount == 0) continue;
            for (int value = start; value < start + k; value++) {
                if (!counts.TryGetValue(value, out int have) || have < amount) return false;
                counts[value] = have - amount;
            }
        }
        return true;
    }
}
