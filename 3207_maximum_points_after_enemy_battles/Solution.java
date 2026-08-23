// LeetCode 3207 - Maximum Points After Enemy Battles
// https://leetcode.com/problems/maximum-points-after-enemy-battles/

import java.util.Arrays;

class Solution {
    public long maximumPoints(int[] enemyEnergies, int currentEnergy) {
        Arrays.sort(enemyEnergies);
        if (currentEnergy < enemyEnergies[0]) return 0;
        long ans = 0;
        for (int i = enemyEnergies.length - 1; i >= 0; i--) {
            ans += currentEnergy / enemyEnergies[0];
            currentEnergy %= enemyEnergies[0];
            currentEnergy += enemyEnergies[i];
        }
        return ans;
    }
}
