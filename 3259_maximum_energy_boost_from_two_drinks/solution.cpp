// LeetCode 3259 - Maximum Energy Boost From Two Drinks
// https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/

#include <algorithm>
#include <cstdint>
#include <vector>

class Solution {
public:
    long long maxEnergyBoost(std::vector<int>& energyDrinkA, std::vector<int>& energyDrinkB) {
        int n = (int)energyDrinkA.size();
        std::vector<int64_t> dpA(n), dpB(n);
        dpA[0] = energyDrinkA[0];
        dpB[0] = energyDrinkB[0];
        if (n == 1) return std::max(dpA[0], dpB[0]);
        dpA[1] = energyDrinkA[1] + dpA[0];
        dpB[1] = energyDrinkB[1] + dpB[0];
        for (int i = 2; i < n; i++) {
            dpA[i] = energyDrinkA[i] + std::max(dpA[i - 1], dpB[i - 2]);
            dpB[i] = energyDrinkB[i] + std::max(dpB[i - 1], dpA[i - 2]);
        }
        return std::max(dpA[n - 1], dpB[n - 1]);
    }
};
