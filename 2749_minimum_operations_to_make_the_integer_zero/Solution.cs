// LeetCode 2749 - Minimum Operations to Make the Integer Zero
// https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/

using System.Numerics;

public class Solution {
    public int MakeTheIntegerZero(int num1, int num2) {
        for (int k = 1; k <= 60; k++) {
            long rem = num1 - 1L * k * num2;
            if (rem < k) continue;
            if (BitOperations.PopCount((ulong)rem) <= k) return k;
        }
        return -1;
    }
}
