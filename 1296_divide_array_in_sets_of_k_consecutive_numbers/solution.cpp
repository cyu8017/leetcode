// LeetCode 1296 - Divide Array in Sets of K Consecutive Numbers
// https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

#include <map>
#include <vector>

class Solution {
public:
    bool isPossibleDivide(std::vector<int>& nums, int k) {
        if (static_cast<int>(nums.size()) % k) {
            return false;
        }
        std::map<int, int> counts;
        for (int x : nums) {
            ++counts[x];
        }
        for (auto it = counts.begin(); it != counts.end(); ++it) {
            int start = it->first;
            int amount = it->second;
            if (amount == 0) {
                continue;
            }
            for (int value = start; value < start + k; ++value) {
                if (counts[value] < amount) {
                    return false;
                }
                counts[value] -= amount;
            }
        }
        return true;
    }
};
