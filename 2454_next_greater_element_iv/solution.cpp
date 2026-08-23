// LeetCode 2454 - Next Greater Element IV
// https://leetcode.com/problems/next-greater-element-iv/

#include <vector>

class Solution {
public:
    std::vector<int> secondGreaterElement(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> ans(n, -1), stack1, stack2;
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            while (!stack2.empty() && nums[stack2.back()] < x) {
                ans[stack2.back()] = x;
                stack2.pop_back();
            }
            std::vector<int> tmp;
            while (!stack1.empty() && nums[stack1.back()] < x) {
                tmp.push_back(stack1.back());
                stack1.pop_back();
            }
            for (int j = (int)tmp.size() - 1; j >= 0; j--) stack2.push_back(tmp[j]);
            stack1.push_back(i);
        }
        return ans;
    }
};
