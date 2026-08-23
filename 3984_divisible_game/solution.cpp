// LeetCode 3984 - Divisible Game
// https://leetcode.com/problems/divisible-game/

#include <cstdint>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int divisibleGame(std::vector<int>& nums) {
        std::unordered_set<int> candidates{2};
        for (int value : nums) {
            for (int divisor = 2; divisor * divisor <= value; divisor++) {
                if (value % divisor != 0) continue;
                candidates.insert(divisor);
                candidates.insert(value / divisor);
            }
            if (value > 1) candidates.insert(value);
        }

        long long bestScore = -(1LL << 62);
        int bestK = 0;
        for (int k : candidates) {
            long long ending = 0, score = 0;
            for (int i = 0; i < (int)nums.size(); i++) {
                int value = nums[i];
                long long contribution = -((long long)value);
                if (value % k == 0) contribution = value;
                if (i == 0 || ending + contribution < contribution) ending = contribution;
                else ending += contribution;
                if (i == 0 || ending > score) score = ending;
            }
            if (score > bestScore || (score == bestScore && k < bestK)) {
                bestScore = score;
                bestK = k;
            }
        }

        const long long mod = 1000000007LL;
        long long answer = (bestScore % mod) * bestK % mod;
        if (answer < 0) answer += mod;
        return (int)answer;
    }
};
