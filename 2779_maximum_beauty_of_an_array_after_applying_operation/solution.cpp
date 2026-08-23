// LeetCode 2779 - Maximum Beauty of an Array After Applying Operation
// https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

#include <algorithm>
#include <vector>

class Solution {
public:
    int maximumBeauty(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        int ans = 0, left = 0;
        for (int right = 0; right < (int)nums.size(); right++) {
            while (nums[right] - nums[left] > 2 * k) left++;
            ans = std::max(ans, right - left + 1);
        }
        return ans;
    }
};
