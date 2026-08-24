// LeetCode 3259 - Maximum Energy Boost From Two Drinks
// https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/

class Solution {
    fun maxEnergyBoost(energyDrinkA: IntArray, energyDrinkB: IntArray): Long {
        var n = energyDrinkA.size
        var dpA = LongArray(n)
        var dpB = LongArray(n)
        dpA[0] = energyDrinkA[0]
        dpB[0] = energyDrinkB[0]
        if (n == 1) return maxOf(dpA[0], dpB[0])
        dpA[1] = energyDrinkA[1] + dpA[0]
        dpB[1] = energyDrinkB[1] + dpB[0]
        for (i in 2 until n) {
            dpA[i] = energyDrinkA[i] + maxOf(dpA[i - 1], dpB[i - 2])
            dpB[i] = energyDrinkB[i] + maxOf(dpB[i - 1], dpA[i - 2])
        }
        return maxOf(dpA[n - 1], dpB[n - 1])
    }
}
