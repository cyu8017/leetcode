// LeetCode 0771 - Jewels and Stones
// https://leetcode.com/problems/jewels-and-stones/

using System.Collections.Generic;

public class Solution {
    public int NumJewelsInStones(string jewels, string stones) {
        var jewelSet = new HashSet<char>(jewels);
        int count = 0;
        foreach (char stone in stones) if (jewelSet.Contains(stone)) count++;
        return count;
    }
}
