// LeetCode 0645 - Set Mismatch
// https://leetcode.com/problems/set-mismatch/

#include <vector>

class Solution {
public:
    std::vector<int> findErrorNums(std::vector<int>& nums) {
        const int n = static_cast<int>(nums.size());
        std::vector<int> seen(n + 1, 0);
        int duplicate = -1;
        int missing = -1;
        for (int value : nums) {
            ++seen[value];
        }
        for (int value = 1; value <= n; ++value) {
            if (seen[value] == 2) {
                duplicate = value;
            } else if (seen[value] == 0) {
                missing = value;
            }
        }
        return {duplicate, missing};
    }
};
