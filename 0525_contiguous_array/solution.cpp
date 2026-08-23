// LeetCode 0525 - Contiguous Array
// https://leetcode.com/problems/contiguous-array/

#include <algorithm>
#include <unordered_map>
#include <vector>

class Solution {
public:
    int findMaxLength(std::vector<int>& nums) {
        std::unordered_map<int, int> counts;
        counts[0] = -1;
        int balance = 0;
        int best = 0;

        for (int index = 0; index < static_cast<int>(nums.size()); ++index) {
            balance += nums[index] == 1 ? 1 : -1;
            const auto found = counts.find(balance);
            if (found != counts.end()) {
                best = std::max(best, index - found->second);
            } else {
                counts[balance] = index;
            }
        }
        return best;
    }
};
