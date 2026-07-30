// LeetCode 1356 - Sort Integers By The Number Of 1 Bits
// https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

using System.Linq;
public class Solution {
    public int[] SortByBits(int[] arr) {
        return arr.OrderBy(x => System.Numerics.BitOperations.PopCount((uint)x)).ThenBy(x => x).ToArray();
    }
}
