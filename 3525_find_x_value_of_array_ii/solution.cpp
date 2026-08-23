// LeetCode 3525 - Find X Value of Array II
// https://leetcode.com/problems/find-x-value-of-array-ii/

#include <vector>

class Solution {
public:
    std::vector<int> resultArray(std::vector<int>& nums, int k, std::vector<std::vector<int>>& queries) {
        int n = (int)nums.size();
        std::vector<int> ans(queries.size());
        for (int qi = 0; qi < (int)queries.size(); qi++) {
            int idx = queries[qi][0], val = queries[qi][1], start = queries[qi][2], x = queries[qi][3];
            nums[idx] = val;
            int prod = 1, cnt = 0;
            for (int i = start; i < n; i++) {
                prod = prod * (nums[i] % k) % k;
                if (prod == x) cnt++;
            }
            ans[qi] = cnt;
        }
        return ans;
    }
};
