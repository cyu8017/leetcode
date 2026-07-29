// LeetCode 1906 - Minimum Absolute Difference Queries
// https://leetcode.com/problems/minimum-absolute-difference-queries/

#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    std::vector<int> minDifference(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        int n = (int)nums.size();
        std::vector<std::vector<int>> pref(n + 1, std::vector<int>(101, 0));
        for (int i = 0; i < n; i++) {
            pref[i + 1] = pref[i];
            pref[i + 1][nums[i]]++;
        }
        std::vector<int> ans;
        for (auto& q : queries) {
            int left = q[0], right = q[1];
            int prev = -1, best = INT_MAX;
            for (int value = 1; value <= 100; value++) {
                if (pref[right + 1][value] - pref[left][value] > 0) {
                    if (prev != -1) best = std::min(best, value - prev);
                    prev = value;
                }
            }
            ans.push_back(best == INT_MAX ? -1 : best);
        }
        return ans;
    }
};
