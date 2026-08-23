// LeetCode 2206 - Divide Array Into Equal Pairs
// https://leetcode.com/problems/divide-array-into-equal-pairs/

using System.Collections.Generic;

public class Solution {
    public bool DivideArray(int[] nums) {
        var freq = new Dictionary<int, int>();
        foreach (int x in nums) {
            freq.TryGetValue(x, out int c);
            freq[x] = c + 1;
        }
        foreach (var c in freq.Values) if (c % 2 != 0) return false;
        return true;
    }
}
