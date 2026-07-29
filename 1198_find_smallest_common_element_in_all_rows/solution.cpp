// LeetCode 1198 - Find Smallest Common Element in All Rows
// https://leetcode.com/problems/find-smallest-common-element-in-all-rows/

#include <algorithm>
#include <climits>
#include <unordered_set>
#include <vector>

class Solution {
public:
    int smallestCommonElement(std::vector<std::vector<int>>& mat) {
        std::unordered_set<int> common(mat[0].begin(), mat[0].end());
        for (size_t r = 1; r < mat.size(); ++r) {
            std::unordered_set<int> row(mat[r].begin(), mat[r].end());
            for (auto it = common.begin(); it != common.end();) {
                if (!row.count(*it)) it = common.erase(it);
                else ++it;
            }
            if (common.empty()) return -1;
        }
        return *std::min_element(common.begin(), common.end());
    }
};
