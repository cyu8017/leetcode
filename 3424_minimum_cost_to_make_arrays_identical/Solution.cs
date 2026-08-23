// LeetCode 3424 - Minimum Cost to Make Arrays Identical
// https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/

using System;

public class Solution {
    public long MinCost(int[] arr, int[] brr, long k) {
        long noSwap = 0;
        for (int i = 0; i < arr.Length; i++) noSwap += Math.Abs(arr[i] - brr[i]);
        int[] a2 = (int[])arr.Clone();
        int[] b2 = (int[])brr.Clone();
        Array.Sort(a2);
        Array.Sort(b2);
        long withSwap = k;
        for (int i = 0; i < a2.Length; i++) withSwap += Math.Abs(a2[i] - b2[i]);
        return noSwap < withSwap ? noSwap : withSwap;
    }
}
