// LeetCode 3848 - Check Digitorial Permutation
// https://leetcode.com/problems/check-digitorial-permutation/

using System;

public class Solution {
    public bool IsDigitorialPermutation(int n) {
        int[] f = new int[10];
        f[0] = 1;
        for (int i = 1; i < 10; i++) f[i] = f[i - 1] * i;
        int x = 0, y = n;
        while (y > 0) {
            x += f[y % 10];
            y /= 10;
        }
        char[] a = x.ToString().ToCharArray();
        char[] b = n.ToString().ToCharArray();
        Array.Sort(a);
        Array.Sort(b);
        return new string(a) == new string(b);
    }
}
