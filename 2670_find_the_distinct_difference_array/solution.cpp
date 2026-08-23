// LeetCode 2670 - Find the Distinct Difference Array
// https://leetcode.com/problems/find-the-distinct-difference-array/

#include <vector>
#include <unordered_set>

class Solution {
public:
    std::vector<int> distinctDifferenceArray(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> suf(n + 1);
        std::unordered_set<int> seen;
        for (int i = n - 1; i >= 0; i--) {
            seen.insert(nums[i]);
            suf[i] = (int)seen.size();
        }
        seen.clear();
        std::vector<int> ans(n);
        for (int i = 0; i < n; i++) {
            seen.insert(nums[i]);
            ans[i] = (int)seen.size() - suf[i + 1];
        }
        return ans;
    }
};
