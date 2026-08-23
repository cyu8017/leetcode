// LeetCode 2442 - Count Number of Distinct Integers After Reverse Operations
// https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

using System.Collections.Generic;

public class Solution {
    public int CountDistinctIntegers(int[] nums) {
        int Rev(int x) {
            int r = 0;
            while (x > 0) {
                r = r * 10 + x % 10;
                x /= 10;
            }
            return r;
        }
        var seen = new HashSet<int>();
        foreach (int x in nums) {
            seen.Add(x);
            seen.Add(Rev(x));
        }
        return seen.Count;
    }
}
