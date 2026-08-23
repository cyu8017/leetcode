// LeetCode 3152 - Special Array II
// https://leetcode.com/problems/special-array-ii/

#include <vector>

class Solution {
public:
    std::vector<bool> isArraySpecial(std::vector<int>& nums, std::vector<std::vector<int>>& queries) {
        int n = (int)nums.size();
        std::vector<int> d(n);
        for (int i = 0; i < n; i++) d[i] = i;
        for (int i = 1; i < n; i++) {
            if (nums[i] % 2 != nums[i - 1] % 2) d[i] = d[i - 1];
        }
        std::vector<bool> ans;
        for (auto& q : queries) ans.push_back(d[q[1]] <= q[0]);
        return ans;
    }
};
