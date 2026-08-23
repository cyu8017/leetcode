// LeetCode 2615 - Sum of Distances
// https://leetcode.com/problems/sum-of-distances/

#include <unordered_map>
#include <vector>

class Solution {
public:
    std::vector<long long> distance(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<long long> ans(n);
        std::unordered_map<int, std::vector<int>> pos;
        for (int i = 0; i < n; ++i) pos[nums[i]].push_back(i);
        for (auto& [_, idxs] : pos) {
            int m = (int)idxs.size();
            std::vector<long long> pref(m + 1);
            for (int i = 0; i < m; ++i) pref[i + 1] = pref[i] + idxs[i];
            for (int j = 0; j < m; ++j) {
                int idx = idxs[j];
                long long left = (long long)j * idx - pref[j];
                long long right = pref[m] - pref[j + 1] - (long long)(m - 1 - j) * idx;
                ans[idx] = left + right;
            }
        }
        return ans;
    }
};
