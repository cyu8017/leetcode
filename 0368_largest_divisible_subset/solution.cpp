// LeetCode 0368 - Largest Divisible Subset
// https://leetcode.com/problems/largest-divisible-subset/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<int> largestDivisibleSubset(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        std::unordered_map<int, std::vector<int>> chains;
        std::vector<int> best;

        for (int num : nums) {
            chains[num] = {num};
            for (const auto& entry : chains) {
                int prev = entry.first;
                if (prev < num && num % prev == 0 && entry.second.size() + 1 > chains[num].size()) {
                    chains[num] = entry.second;
                    chains[num].push_back(num);
                }
            }
            if (chains[num].size() > best.size()) {
                best = chains[num];
            }
        }

        return best;
    }
};
