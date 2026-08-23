// LeetCode 3514 - Number of Unique XOR Triplets II
// https://leetcode.com/problems/number-of-unique-xor-triplets-ii/

using System;

public class Solution {
    public int UniqueXorTriplets(int[] nums) {
        int mx = 0;
        foreach (int v in nums) mx = Math.Max(mx, v);
        mx <<= 1;
        bool[] st = new bool[mx];
        foreach (int a in nums) foreach (int b in nums) st[a ^ b] = true;
        int[] s = new int[mx];
        for (int ab = 0; ab < mx; ab++) {
            if (st[ab]) foreach (int c in nums) s[ab ^ c] = 1;
        }
        int ans = 0;
        foreach (int v in s) ans += v;
        return ans;
    }
}
