// LeetCode 0078 - Subsets
// https://leetcode.com/problems/subsets/

#include <vector>

class Solution {
public:
    std::vector<std::vector<int>> subsets(std::vector<int>& nums) {
        std::vector<std::vector<int>> result = {{}};

        for (int num : nums) {
            int size = static_cast<int>(result.size());
            for (int i = 0; i < size; i++) {
                std::vector<int> subset = result[i];
                subset.push_back(num);
                result.push_back(subset);
            }
        }

        return result;
    }
};
