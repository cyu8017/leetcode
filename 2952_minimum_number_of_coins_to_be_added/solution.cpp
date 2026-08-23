// LeetCode 2952 - Minimum Number of Coins to be Added
// https://leetcode.com/problems/minimum-number-of-coins-to-be-added/

#include <algorithm>
#include <vector>

class Solution {
public:
    int minimumAddedCoins(std::vector<int>& coins, int target) {
        std::sort(coins.begin(), coins.end());
        int ans = 0, reach = 0, i = 0;
        while (reach < target) {
            if (i < (int)coins.size() && coins[i] <= reach + 1) {
                reach += coins[i];
                i++;
            } else {
                reach += reach + 1;
                ans++;
            }
        }
        return ans;
    }
};
