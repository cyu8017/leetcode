// LeetCode 3207 - Maximum Points After Enemy Battles
// https://leetcode.com/problems/maximum-points-after-enemy-battles/

#include <vector>
#include <algorithm>

class Solution {
public:
    long long maximumPoints(std::vector<int>& enemyEnergies, int currentEnergy) {
        std::sort(enemyEnergies.begin(), enemyEnergies.end());
        if (currentEnergy < enemyEnergies[0]) return 0;
        long long ans = 0;
        for (int i = (int)enemyEnergies.size() - 1; i >= 0; i--) {
            ans += currentEnergy / enemyEnergies[0];
            currentEnergy %= enemyEnergies[0];
            currentEnergy += enemyEnergies[i];
        }
        return ans;
    }
};
