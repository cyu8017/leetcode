// LeetCode 1561 - Maximum Number of Coins You Can Get
// https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maxCoins(std::vector<int>& piles) {
        std::sort(piles.begin(), piles.end());
        int answer = 0;
        for (std::size_t i = piles.size() / 3; i < piles.size(); i += 2) {
            answer += piles[i];
        }
        return answer;
    }
};
