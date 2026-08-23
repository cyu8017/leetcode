// LeetCode 3759 - Count Elements With At Least K Greater Values
// https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/

#include <algorithm>
#include <vector>

class Solution {
public:
    int countElements(std::vector<int>& nums, int k) {
        int n = (int)nums.size();
        if (k == 0) return n;
        std::sort(nums.begin(), nums.end());
        int ans = 0;
        for (int i = 0; i < n - k; i++) {
            if (nums[n - k] > nums[i]) ans++;
        }
        return ans;
    }
};
