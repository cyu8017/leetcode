// LeetCode 1177 - Can Make Palindrome from Substring
// https://leetcode.com/problems/can-make-palindrome-from-substring/

using System;
using System.Collections.Generic;
using System.Numerics;

public class Solution {
    public IList<bool> CanMakePaliQueries(string s, int[][] queries) {
        var prefix = new List<int> { 0 };
        int mask = 0;
        foreach (char ch in s) {
            mask ^= 1 << (ch - 'a');
            prefix.Add(mask);
        }
        var ans = new List<bool>();
        foreach (var q in queries) {
            int left = q[0], right = q[1], k = q[2];
            int bits = BitOperations.PopCount((uint)(prefix[right + 1] ^ prefix[left]));
            ans.Add(bits / 2 <= k);
        }
        return ans;
    }
}
