// LeetCode 3289 - The Two Sneaky Numbers of Digitville
// https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<int> getSneakyNumbers(std::vector<int>& nums) {
        std::unordered_set<int> seen;
        std::vector<int> ans;
        for (int x : nums) {
            if (seen.count(x)) ans.push_back(x);
            else seen.insert(x);
        }
        return ans;
    }
};
