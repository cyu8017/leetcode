// LeetCode 1950 - Maximum of Minimum Values in All Subarrays
#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> findMaximums(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> left(n, -1), right(n, n), stack;
        for (int i = 0; i < n; i++) {
            while (!stack.empty() && nums[stack.back()] >= nums[i]) stack.pop_back();
            left[i] = stack.empty() ? -1 : stack.back();
            stack.push_back(i);
        }
        stack.clear();
        for (int i = n - 1; i >= 0; i--) {
            while (!stack.empty() && nums[stack.back()] >= nums[i]) stack.pop_back();
            right[i] = stack.empty() ? n : stack.back();
            stack.push_back(i);
        }
        std::vector<int> ans(n, 0);
        for (int i = 0; i < n; i++) {
            int length = right[i] - left[i] - 1;
            ans[length - 1] = std::max(ans[length - 1], nums[i]);
        }
        for (int i = n - 2; i >= 0; i--) ans[i] = std::max(ans[i], ans[i + 1]);
        return ans;
    }
};
