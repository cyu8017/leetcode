#include <algorithm>
#include <climits>
#include <vector>

class Solution {
public:
    int maxValueAfterReverse(std::vector<int>& nums) {
        int n = (int)nums.size();
        int total = 0;
        for (int i = 0; i + 1 < n; ++i) total += std::abs(nums[i] - nums[i + 1]);
        int gain = 0;
        for (int i = 0; i + 1 < n; ++i) {
            gain = std::max(gain, std::abs(nums[0] - nums[i + 1]) - std::abs(nums[i] - nums[i + 1]));
            gain = std::max(gain, std::abs(nums[n - 1] - nums[i]) - std::abs(nums[i] - nums[i + 1]));
        }
        int mn = INT_MAX, mx = INT_MIN;
        for (int i = 0; i + 1 < n; ++i) {
            mn = std::min(mn, std::max(nums[i], nums[i + 1]));
            mx = std::max(mx, std::min(nums[i], nums[i + 1]));
        }
        return total + std::max(gain, 2 * (mx - mn));
    }
};
