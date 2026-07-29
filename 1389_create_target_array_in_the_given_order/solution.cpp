#include <vector>

class Solution {
public:
    std::vector<int> createTargetArray(std::vector<int>& nums, std::vector<int>& index) {
        std::vector<int> out;
        for (size_t i = 0; i < nums.size(); ++i)
            out.insert(out.begin() + index[i], nums[i]);
        return out;
    }
};
