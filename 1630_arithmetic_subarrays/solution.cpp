// LeetCode 1630 - Arithmetic Subarrays
// https://leetcode.com/problems/arithmetic-subarrays/

#include <algorithm>
#include <unordered_set>
#include <vector>

class Solution {
public:
    std::vector<bool> checkArithmeticSubarrays(std::vector<int>& nums, std::vector<int>& l, std::vector<int>& r) {
        std::vector<bool> ans;
        ans.reserve(l.size());
        for (size_t t = 0; t < l.size(); ++t) {
            std::vector<int> x(nums.begin() + l[t], nums.begin() + r[t] + 1);
            std::sort(x.begin(), x.end());
            if (x.size() < 3) {
                ans.push_back(true);
                continue;
            }
            std::unordered_set<int> diffs;
            for (size_t i = 0; i + 1 < x.size(); ++i) {
                diffs.insert(x[i + 1] - x[i]);
            }
            ans.push_back(diffs.size() == 1);
        }
        return ans;
    }
};
