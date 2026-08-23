// LeetCode 2343 - Query Kth Smallest Trimmed Number
// https://leetcode.com/problems/query-kth-smallest-trimmed-number/

#include <algorithm>
#include <string>
#include <vector>

class Solution {
public:
    std::vector<int> smallestTrimmedNumbers(std::vector<std::string>& nums, std::vector<std::vector<int>>& queries) {
        std::vector<int> ans(queries.size());
        for (int qi = 0; qi < (int)queries.size(); qi++) {
            int k = queries[qi][0], trim = queries[qi][1];
            std::vector<std::pair<std::string, int>> arr;
            arr.reserve(nums.size());
            for (int i = 0; i < (int)nums.size(); i++) {
                arr.push_back({nums[i].substr(nums[i].size() - trim), i});
            }
            std::stable_sort(arr.begin(), arr.end(), [](const auto& a, const auto& b) {
                if (a.first == b.first) return a.second < b.second;
                return a.first < b.first;
            });
            ans[qi] = arr[k - 1].second;
        }
        return ans;
    }
};
