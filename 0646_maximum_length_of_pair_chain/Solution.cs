// LeetCode 0646 - Maximum Length of Pair Chain
// https://leetcode.com/problems/maximum-length-of-pair-chain/

using System;

public class Solution {
    public int FindLongestChain(int[][] pairs) {
        Array.Sort(pairs, (a, b) => a[1].CompareTo(b[1]));
        int length = 0, currentEnd = int.MinValue;
        foreach (var pair in pairs) {
            if (pair[0] > currentEnd) {
                ++length;
                currentEnd = pair[1];
            }
        }
        return length;
    }
}
