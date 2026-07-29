#include <algorithm>
#include <vector>

class Solution {
public:
    int longestSubarray(std::vector<int>& nums) {
        int left = 0, zeros = 0, ans = 0;
        for (int right = 0; right < (int)nums.size(); ++right) {
            zeros += nums[right] == 0;
            while (zeros > 1) zeros -= nums[left++] == 0;
            ans = std::max(ans, right - left);
        }
        return ans;
    }
};
