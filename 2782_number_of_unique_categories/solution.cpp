// LeetCode 2782 - Number of Unique Categories
// https://leetcode.com/problems/number-of-unique-categories/

#include <unordered_set>
#include <vector>

class Solution {
public:
    int numberOfCategories(int n, std::vector<int>& categoryHandler) {
        (void)n;
        return (int)std::unordered_set<int>(categoryHandler.begin(), categoryHandler.end()).size();
    }
};
