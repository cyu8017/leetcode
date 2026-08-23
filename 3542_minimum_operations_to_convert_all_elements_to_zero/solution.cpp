// LeetCode 3542 - Minimum Operations to Convert All Elements to Zero
// https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        std::vector<int> stk;
        int ans = 0;
        for (int x : nums) {
            while (!stk.empty() && stk.back() > x) {
                ans++;
                stk.pop_back();
            }
            if (x != 0 && (stk.empty() || stk.back() != x)) stk.push_back(x);
        }
        ans += (int)stk.size();
        return ans;
    }
};
