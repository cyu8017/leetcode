// LeetCode 0869 - Reordered Power of 2
// https://leetcode.com/problems/reordered-power-of-2/

using System;

public class Solution {
    public bool ReorderedPowerOf2(int n) {
        string Sig(int x) {
            char[] s = x.ToString().ToCharArray();
            Array.Sort(s);
            return new string(s);
        }
        string target = Sig(n);
        for (int i = 0; i < 31; i++)
            if (Sig(1 << i) == target) return true;
        return false;
    }
}
