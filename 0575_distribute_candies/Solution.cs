// LeetCode 0575 - Distribute Candies
// https://leetcode.com/problems/distribute-candies/

using System.Collections.Generic;

public class Solution {
    public int DistributeCandies(int[] candyType) {
        var unique = new HashSet<int>(candyType);
        return System.Math.Min(unique.Count, candyType.Length / 2);
    }
}
