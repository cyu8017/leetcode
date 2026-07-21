// LeetCode 1899 - Merge Triplets to Form Target Triplet
// https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

#include <algorithm>
#include <vector>

class Solution {
public:
    bool mergeTriplets(std::vector<std::vector<int>>& triplets, std::vector<int>& target) {
        std::vector<int> merged = {0, 0, 0};
        for (const auto& t : triplets) {
            if (t[0] <= target[0] && t[1] <= target[1] && t[2] <= target[2]) {
                merged[0] = std::max(merged[0], t[0]);
                merged[1] = std::max(merged[1], t[1]);
                merged[2] = std::max(merged[2], t[2]);
            }
        }
        return merged == target;
    }
};
