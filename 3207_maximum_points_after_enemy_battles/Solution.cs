// LeetCode 3207 - Maximum Points After Enemy Battles
// https://leetcode.com/problems/maximum-points-after-enemy-battles/

using System;

public class Solution {
    public long MaximumPoints(int[] enemyEnergies, int currentEnergy) {
        Array.Sort(enemyEnergies);
        if (currentEnergy < enemyEnergies[0]) return 0;
        long ans = 0;
        for (int i = enemyEnergies.Length - 1; i >= 0; i--) {
            ans += currentEnergy / enemyEnergies[0];
            currentEnergy %= enemyEnergies[0];
            currentEnergy += enemyEnergies[i];
        }
        return ans;
    }
}
