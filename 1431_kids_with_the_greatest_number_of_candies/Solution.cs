// LeetCode 1431 - Kids With The Greatest Number Of Candies
// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

using System.Collections.Generic;
using System.Linq;
public class Solution {
    public IList<bool> KidsWithCandies(int[] candies, int extraCandies) {
        int maximum = candies.Max();
        return candies.Select(v => v + extraCandies >= maximum).ToList();
    }
}
