#include <algorithm>
#include <vector>

class Solution {
public:
    int maxProduct(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int a = nums[nums.size() - 2], b = nums.back();
        return (a - 1) * (b - 1);
    }
};
