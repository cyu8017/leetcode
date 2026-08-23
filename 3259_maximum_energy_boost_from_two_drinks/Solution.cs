// LeetCode 3259 - Maximum Energy Boost From Two Drinks
// https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/

using System;

public class Solution {
    public long MaxEnergyBoost(int[] energyDrinkA, int[] energyDrinkB) {
        int n = energyDrinkA.Length;
        long[] dpA = new long[n], dpB = new long[n];
        dpA[0] = energyDrinkA[0];
        dpB[0] = energyDrinkB[0];
        if (n == 1) return Math.Max(dpA[0], dpB[0]);
        dpA[1] = energyDrinkA[1] + dpA[0];
        dpB[1] = energyDrinkB[1] + dpB[0];
        for (int i = 2; i < n; i++) {
            dpA[i] = energyDrinkA[i] + Math.Max(dpA[i - 1], dpB[i - 2]);
            dpB[i] = energyDrinkB[i] + Math.Max(dpB[i - 1], dpA[i - 2]);
        }
        return Math.Max(dpA[n - 1], dpB[n - 1]);
    }
}
