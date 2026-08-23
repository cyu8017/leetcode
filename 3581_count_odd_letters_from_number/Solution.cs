// LeetCode 3581 - Count Odd Letters from Number
// https://leetcode.com/problems/count-odd-letters-from-number/

using System.Collections.Generic;
using System.Numerics;

public class Solution {
    public int CountOddLetters(int n) {
        var d = new Dictionary<int, string> {
            {0, "zero"}, {1, "one"}, {2, "two"}, {3, "three"}, {4, "four"},
            {5, "five"}, {6, "six"}, {7, "seven"}, {8, "eight"}, {9, "nine"},
        };
        uint mask = 0;
        while (n > 0) {
            int x = n % 10;
            n /= 10;
            foreach (char c in d[x]) mask ^= 1u << (c - 'a');
        }
        return BitOperations.PopCount(mask);
    }
}
