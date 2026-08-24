// LeetCode 3207 - Maximum Points After Enemy Battles
// https://leetcode.com/problems/maximum-points-after-enemy-battles/

class Solution {
    fun maximumPoints(enemyEnergies: IntArray, currentEnergy: Int): Long {
        enemyEnergies.sort()
        if (currentEnergy < enemyEnergies[0]) return 0
        var ans = 0
        for (i in enemyEnergies.size - 1 downTo 0) {
            ans += currentEnergy / enemyEnergies[0]
            currentEnergy %= enemyEnergies[0]
            currentEnergy += enemyEnergies[i]
        }
        return ans
    }
}
