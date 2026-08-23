// LeetCode 3912 - Valid Elements In An Array
// https://leetcode.com/problems/valid-elements-in-an-array/

#include <algorithm>
#include <vector>

class Solution {
public:
    std::vector<int> findValidElements(std::vector<int>& nums) {
        int n = (int)nums.size();
        std::vector<int> right(n);
        right[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) right[i] = std::max(right[i + 1], nums[i]);
        int left = 0;
        std::vector<int> ans;
        for (int i = 0; i < n; i++) {
            int x = nums[i];
            if (x > left || i == n - 1 || x > right[i + 1]) ans.push_back(x);
            left = std::max(left, x);
        }
        return ans;
    }
};
