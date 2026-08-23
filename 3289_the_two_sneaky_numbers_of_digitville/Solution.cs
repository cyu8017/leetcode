// LeetCode 3289 - The Two Sneaky Numbers of Digitville
// https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

using System.Collections.Generic;

public class Solution {
    public int[] GetSneakyNumbers(int[] nums) {
        var seen = new HashSet<int>();
        var ans = new List<int>();
        foreach (int x in nums) {
            if (seen.Contains(x)) ans.Add(x);
            else seen.Add(x);
        }
        return ans.ToArray();
    }
}
