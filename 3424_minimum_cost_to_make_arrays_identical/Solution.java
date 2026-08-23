// LeetCode 3424 - Minimum Cost to Make Arrays Identical
// https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/

import java.util.Arrays;

class Solution {
    public long minCost(int[] arr, int[] brr, long k) {
        long noSwap = 0;
        for (int i = 0; i < arr.length; i++) noSwap += Math.abs(arr[i] - brr[i]);
        int[] a2 = arr, b2 = brr;
        Arrays.sort(a2);
        Arrays.sort(b2);
        long withSwap = k;
        for (int i = 0; i < a2.length; i++) withSwap += Math.abs(a2[i] - b2[i]);
        return noSwap < withSwap ? noSwap : withSwap;
    }
}
